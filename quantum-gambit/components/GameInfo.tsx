'use client';

import { Color } from 'chess.js';

interface GameInfoProps {
  currentPlayer: Color;
  turnCount: number;
  inCheck: boolean;
  isGameOver: boolean;
}

export default function GameInfo({
  currentPlayer,
  turnCount,
  inCheck,
  isGameOver,
}: GameInfoProps) {
  return (
    <div className="pixel-border p-4 bg-nes-dark">
      <div className="pixel-font text-xs mb-3">
        🎮 GAME STATUS
      </div>

      <div className="space-y-2 text-sm">
        <div className="flex justify-between">
          <span>Turn:</span>
          <span className="pixel-font text-evolution-gold">{Math.ceil(turnCount / 2)}</span>
        </div>

        <div className="flex justify-between">
          <span>Player:</span>
          <span className="pixel-font">
            {currentPlayer === 'w' ? '⚪ WHITE' : '⚫ BLACK'}
          </span>
        </div>

        {inCheck && (
          <div className="pixel-font text-xs text-pixel-red pulse">
            ⚠️ CHECK!
          </div>
        )}

        {isGameOver && (
          <div className="pixel-font text-xs text-evolution-gold pulse">
            ⚡ GAME OVER
          </div>
        )}
      </div>
    </div>
  );
}
