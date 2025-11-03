'use client';

import { Square, Piece } from 'chess.js';
import ChessPiece from './ChessPiece';
import { PieceEvolution } from '@/lib/types';

interface ChessSquareProps {
  square: Square;
  piece: Piece | null;
  isLight: boolean;
  isSelected: boolean;
  isValidMove: boolean;
  isGravityWell: boolean;
  evolution?: PieceEvolution;
  onClick: () => void;
}

export default function ChessSquare({
  square,
  piece,
  isLight,
  isSelected,
  isValidMove,
  isGravityWell,
  evolution,
  onClick,
}: ChessSquareProps) {
  const getBgColor = () => {
    if (isGravityWell) return 'bg-purple-800 animate-pulse';
    if (isSelected) return 'bg-flux-blue';
    if (isValidMove) return 'bg-green-600';
    return isLight ? 'bg-nes-light' : 'bg-nes-accent';
  };

  return (
    <div
      className={`
        ${getBgColor()}
        w-16 h-16 flex items-center justify-center cursor-pointer
        border border-nes-dark hover:brightness-110 transition-all
        ${isGravityWell ? 'shake' : ''}
      `}
      onClick={onClick}
    >
      {piece && (
        <ChessPiece
          type={evolution?.evolvedType || piece.type}
          color={piece.color}
          isEvolved={!!evolution}
        />
      )}
      {isValidMove && !piece && (
        <div className="w-3 h-3 rounded-full bg-green-400 opacity-70" />
      )}
    </div>
  );
}
