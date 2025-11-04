'use client';

import { Square } from 'chess.js';
import ChessSquare from './ChessSquare';
import { QuantumChess } from '@/lib/quantumChess';

interface ChessBoardProps {
  game: QuantumChess;
  selectedSquare: Square | null;
  validMoves: Square[];
  onSquareClick: (square: Square) => void;
}

const GRAVITY_WELL_SQUARES: Square[] = ['d4', 'd5', 'e4', 'e5'];

export default function ChessBoard({
  game,
  selectedSquare,
  validMoves,
  onSquareClick,
}: ChessBoardProps) {
  const board = game.getGame().board();
  const state = game.getState();
  const isGravityWellActive = state.gravityWellActive;

  const renderBoard = () => {
    const squares = [];

    // Render from rank 8 to rank 1 (top to bottom)
    for (let rank = 7; rank >= 0; rank--) {
      for (let file = 0; file < 8; file++) {
        const square = `${String.fromCharCode(97 + file)}${rank + 1}` as Square;
        const piece = board[rank][file];
        const isLight = (rank + file) % 2 === 1;
        const isSelected = selectedSquare === square;
        const isValidMove = validMoves.includes(square);
        const isGravityWell = isGravityWellActive && GRAVITY_WELL_SQUARES.includes(square);
        const evolution = state.pieceEvolutions.get(square);

        squares.push(
          <ChessSquare
            key={square}
            square={square}
            piece={piece}
            isLight={isLight}
            isSelected={isSelected}
            isValidMove={isValidMove}
            isGravityWell={isGravityWell}
            evolution={evolution}
            onClick={() => onSquareClick(square)}
          />
        );
      }
    }

    return squares;
  };

  return (
    <div className="relative">
      <div className="grid grid-cols-8 gap-0 pixel-border bg-nes-dark p-2 scanlines">
        {renderBoard()}
      </div>

      {/* Rank labels */}
      <div className="absolute -left-8 top-2 flex flex-col justify-around h-full pixel-font text-xs">
        {[8, 7, 6, 5, 4, 3, 2, 1].map(rank => (
          <div key={rank} className="h-16 flex items-center">
            {rank}
          </div>
        ))}
      </div>

      {/* File labels */}
      <div className="flex justify-around mt-2 pixel-font text-xs">
        {['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'].map(file => (
          <div key={file} className="w-16 text-center">
            {file}
          </div>
        ))}
      </div>
    </div>
  );
}
