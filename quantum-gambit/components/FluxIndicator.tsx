'use client';

import { FluxEvent } from '@/lib/types';

interface FluxIndicatorProps {
  activeFlux: FluxEvent | null;
  nextFluxTurn: number;
  currentTurn: number;
}

export default function FluxIndicator({
  activeFlux,
  nextFluxTurn,
  currentTurn,
}: FluxIndicatorProps) {
  const turnsUntilFlux = nextFluxTurn - currentTurn;

  return (
    <div className="space-y-4">
      {/* Active Flux Event */}
      {activeFlux ? (
        <div className="pixel-border p-4 bg-nes-accent glow-blue">
          <div className="pixel-font text-xs text-flux-blue mb-2">
            ⚡ ACTIVE FLUX
          </div>
          <div className="pixel-font text-sm mb-2">
            {activeFlux.name}
          </div>
          <div className="text-xs mb-2">
            {activeFlux.description}
          </div>
          <div className="pixel-font text-xs text-evolution-gold">
            {activeFlux.turnsRemaining} turns remaining
          </div>
        </div>
      ) : (
        <div className="pixel-border p-4 bg-nes-accent">
          <div className="pixel-font text-xs mb-2">
            ⚪ NO ACTIVE FLUX
          </div>
          <div className="text-xs">
            Standard chess rules apply
          </div>
        </div>
      )}

      {/* Next Flux Timer */}
      <div className="pixel-border p-4 bg-nes-dark">
        <div className="pixel-font text-xs mb-2">
          🎲 NEXT QUANTUM FLUX
        </div>
        <div className="flex items-center gap-2">
          <div className="pixel-font text-2xl text-evolution-gold">
            {turnsUntilFlux}
          </div>
          <div className="text-xs">
            turns until<br />next flux event
          </div>
        </div>
        <div className="mt-2 w-full bg-nes-accent rounded-full h-2">
          <div
            className="bg-flux-blue h-2 rounded-full transition-all"
            style={{ width: `${((5 - turnsUntilFlux) / 5) * 100}%` }}
          />
        </div>
      </div>
    </div>
  );
}
