'use client';

import { useState, useEffect } from 'react';
import { Square } from 'chess.js';
import { QuantumChess } from '@/lib/quantumChess';
import ChessBoard from '@/components/ChessBoard';
import FluxIndicator from '@/components/FluxIndicator';
import GameInfo from '@/components/GameInfo';
import EvolutionTracker from '@/components/EvolutionTracker';

export default function Home() {
  const [game, setGame] = useState<QuantumChess | null>(null);
  const [selectedSquare, setSelectedSquare] = useState<Square | null>(null);
  const [validMoves, setValidMoves] = useState<Square[]>([]);
  const [, forceUpdate] = useState({});

  // Initialize game
  useEffect(() => {
    const newGame = new QuantumChess();
    setGame(newGame);
  }, []);

  const refresh = () => forceUpdate({});

  const handleSquareClick = (square: Square) => {
    if (!game) return;

    // If no square is selected, select this square
    if (!selectedSquare) {
      const piece = game.getGame().get(square);
      if (piece && piece.color === game.turn()) {
        setSelectedSquare(square);
        const moves = game.moves({ square });
        setValidMoves(moves.map(m => m.to as Square));
      }
      return;
    }

    // If clicking the same square, deselect
    if (selectedSquare === square) {
      setSelectedSquare(null);
      setValidMoves([]);
      return;
    }

    // If clicking a valid move, make the move
    if (validMoves.includes(square)) {
      const move = game.move(selectedSquare, square);

      if (move) {
        console.log('Move made:', move);
        setSelectedSquare(null);
        setValidMoves([]);
        refresh();
      }
      return;
    }

    // If clicking another piece of the same color, select it
    const piece = game.getGame().get(square);
    if (piece && piece.color === game.turn()) {
      setSelectedSquare(square);
      const moves = game.moves({ square });
      setValidMoves(moves.map(m => m.to as Square));
    } else {
      setSelectedSquare(null);
      setValidMoves([]);
    }
  };

  const handleReset = () => {
    if (game) {
      game.reset();
      setSelectedSquare(null);
      setValidMoves([]);
      refresh();
    }
  };

  if (!game) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="pixel-font text-2xl pulse">LOADING...</div>
      </div>
    );
  }

  const state = game.getState();

  return (
    <main className="min-h-screen p-8 bg-nes-dark">
      {/* Header */}
      <header className="text-center mb-8">
        <h1 className="pixel-font text-3xl mb-2 text-flux-blue">
          QUANTUM GAMBIT 8-BIT
        </h1>
        <p className="text-sm text-nes-light">
          Where Chess Meets Quantum Chaos
        </p>
      </header>

      {/* Main Game Layout */}
      <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Sidebar - Game Info */}
        <div className="space-y-4">
          <GameInfo
            currentPlayer={game.turn()}
            turnCount={state.turnCount}
            inCheck={game.inCheck()}
            isGameOver={game.isGameOver()}
          />

          <EvolutionTracker evolutions={state.pieceEvolutions} />

          {/* Controls */}
          <div className="space-y-2">
            <button
              onClick={handleReset}
              className="pixel-button w-full"
            >
              🔄 NEW GAME
            </button>

            <button
              onClick={() => alert('Coming soon: Rules & Tutorial!')}
              className="pixel-button w-full"
            >
              📖 RULES
            </button>
          </div>

          {/* Legend */}
          <div className="pixel-border p-4 bg-nes-accent text-xs">
            <div className="pixel-font mb-2">LEGEND</div>
            <div className="space-y-1">
              <div>⚜ Archon (Pawn evo)</div>
              <div>⚔ Phantom Knight</div>
              <div>🎯 Sniper Bishop</div>
              <div>🛡 Royal Guard (Rook evo)</div>
            </div>
          </div>
        </div>

        {/* Center - Chess Board */}
        <div className="flex items-start justify-center">
          <ChessBoard
            game={game}
            selectedSquare={selectedSquare}
            validMoves={validMoves}
            onSquareClick={handleSquareClick}
          />
        </div>

        {/* Right Sidebar - Flux Info */}
        <div className="space-y-4">
          <FluxIndicator
            activeFlux={state.activeFlux}
            nextFluxTurn={state.nextFluxTurn}
            currentTurn={state.turnCount}
          />

          {/* Flux Events Guide */}
          <div className="pixel-border p-4 bg-nes-dark text-xs">
            <div className="pixel-font mb-3 text-flux-blue">
              ⚡ FLUX EVENTS
            </div>
            <div className="space-y-2">
              <div>
                <div className="font-bold">🌀 Gravity Well</div>
                <div className="text-gray-400">Center squares destroy adjacent pieces</div>
              </div>
              <div>
                <div className="font-bold">👑 Anarchy Mode</div>
                <div className="text-gray-400">All pieces move like Queens</div>
              </div>
              <div>
                <div className="font-bold">🔥 Elemental: Fire</div>
                <div className="text-gray-400">Captures damage nearby pieces</div>
              </div>
              <div>
                <div className="font-bold">🔀 Realm Shift</div>
                <div className="text-gray-400">Split board with different rules</div>
              </div>
              <div>
                <div className="font-bold">⏰ Chrono-Sync</div>
                <div className="text-gray-400">Unmoved pieces can teleport</div>
              </div>
            </div>
          </div>

          {/* Tips */}
          <div className="pixel-border p-4 bg-nes-accent text-xs">
            <div className="pixel-font mb-2">💡 TIPS</div>
            <ul className="space-y-1 list-disc list-inside">
              <li>Flux events trigger every 5 turns</li>
              <li>Pawns evolve at back rank</li>
              <li>Knights evolve after 3 forks</li>
              <li>Plan around the Flux timer!</li>
            </ul>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="text-center mt-12 text-xs text-gray-500">
        <p>Built with Next.js, TypeScript, and chess.js</p>
        <p className="pixel-font mt-2">Press START to play! 🎮</p>
      </footer>
    </main>
  );
}
