import { logger } from './logger.js';

function backoffMs(attempt) {
  const base = 500 * 2 ** attempt;
  const jitter = Math.random() * 250;
  return Math.min(base + jitter, 30_000);
}

export function createTaskQueue({ concurrency = 3, maxRetries = 5, isRetryable = () => false } = {}) {
  const pending = [];
  let active = 0;

  function runNext() {
    if (active >= concurrency || pending.length === 0) return;
    const task = pending.shift();
    active++;

    task
      .handler()
      .then(task.resolve)
      .catch((err) => {
        if (task.attempt < maxRetries && isRetryable(err)) {
          const delay = backoffMs(task.attempt);
          logger.warn('Retrying task after failure', {
            attempt: task.attempt + 1,
            maxRetries,
            delayMs: Math.round(delay),
            error: err.message,
          });
          setTimeout(() => {
            pending.push({ ...task, attempt: task.attempt + 1 });
            runNext();
          }, delay);
        } else {
          task.reject(err);
        }
      })
      .finally(() => {
        active--;
        runNext();
      });
  }

  return {
    enqueue(handler) {
      return new Promise((resolve, reject) => {
        pending.push({ handler, resolve, reject, attempt: 0 });
        runNext();
      });
    },
  };
}
