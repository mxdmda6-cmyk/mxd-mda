'use client';

import { PieceEvolution } from '@/lib/types';

interface EvolutionTrackerProps {
  evolutions: Map<string, PieceEvolution>;
}

const EVOLUTION_NAMES: Record<string, string> = {
  archon: 'ARCHON',
  phantom_knight: 'PHANTOM KNIGHT',
  sniper_bishop: 'SNIPER BISHOP',
  royal_guard: 'ROYAL GUARD',
};

const EVOLUTION_ICONS: Record<string, string> = {
  archon: '⚜',
  phantom_knight: '⚔',
  sniper_bishop: '🎯',
  royal_guard: '🛡',
};

export default function EvolutionTracker({ evolutions }: EvolutionTrackerProps) {
  const evolutionList = Array.from(evolutions.values());

  if (evolutionList.length === 0) {
    return (
      <div className="pixel-border p-4 bg-nes-accent">
        <div className="pixel-font text-xs mb-2">
          ✨ EVOLUTIONS
        </div>
        <div className="text-xs text-gray-400">
          No pieces evolved yet
        </div>
      </div>
    );
  }

  return (
    <div className="pixel-border p-4 bg-nes-accent">
      <div className="pixel-font text-xs mb-3 text-evolution-gold">
        ✨ ACTIVE EVOLUTIONS
      </div>

      <div className="space-y-2">
        {evolutionList.map((evo, idx) => (
          <div
            key={idx}
            className="flex items-center gap-2 text-xs bg-nes-dark p-2 rounded"
          >
            <span className="text-xl">
              {EVOLUTION_ICONS[evo.evolvedType]}
            </span>
            <div>
              <div className="pixel-font text-evolution-gold">
                {EVOLUTION_NAMES[evo.evolvedType]}
              </div>
              <div className="text-gray-400">
                {evo.square} • {evo.color === 'w' ? 'White' : 'Black'}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
