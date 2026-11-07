const LEVELS = { debug: 10, info: 20, warn: 30, error: 40 };

const currentLevel = LEVELS[(process.env.LOG_LEVEL || 'info').toLowerCase()] ?? LEVELS.info;

function log(level, message, meta) {
  if (LEVELS[level] < currentLevel) return;
  const entry = {
    timestamp: new Date().toISOString(),
    level,
    message,
    ...(meta ? { meta } : {}),
  };
  const line = JSON.stringify(entry);
  if (level === 'error' || level === 'warn') {
    process.stderr.write(line + '\n');
  } else {
    process.stdout.write(line + '\n');
  }
}

export const logger = {
  debug: (message, meta) => log('debug', message, meta),
  info: (message, meta) => log('info', message, meta),
  warn: (message, meta) => log('warn', message, meta),
  error: (message, meta) => log('error', message, meta),
};
