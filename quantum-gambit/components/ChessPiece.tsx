'use client';

import { PieceSymbol, Color } from 'chess.js';
import { EvolvedPieceType } from '@/lib/types';

interface ChessPieceProps {
  type: PieceSymbol | EvolvedPieceType;
  color: Color;
  isEvolved?: boolean;
}

const PIECE_SYMBOLS: Record<string, string> = {
  // Standard pieces
  'w-p': '♙',
  'w-n': '♘',
  'w-b': '♗',
  'w-r': '♖',
  'w-q': '♕',
  'w-k': '♔',
  'b-p': '♟',
  'b-n': '♞',
  'b-b': '♝',
  'b-r': '♜',
  'b-q': '♛',
  'b-k': '♚',
  // Evolved pieces (with special styling)
  'w-archon': '⚜',
  'b-archon': '⚜',
  'w-phantom_knight': '⚔',
  'b-phantom_knight': '⚔',
  'w-sniper_bishop': '🎯',
  'b-sniper_bishop': '🎯',
  'w-royal_guard': '🛡',
  'b-royal_guard': '🛡',
};

export default function ChessPiece({ type, color, isEvolved = false }: ChessPieceProps) {
  const pieceKey = `${color}-${type}`;
  const symbol = PIECE_SYMBOLS[pieceKey] || '?';

  return (
    <div className={`text-4xl select-none ${isEvolved ? 'glow-gold' : ''}`}>
      {symbol}
    </div>
  );
}
