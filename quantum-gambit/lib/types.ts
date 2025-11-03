import { Square, PieceSymbol, Color } from 'chess.js';

export type FluxEventType =
  | 'gravity_well'
  | 'anarchy_mode'
  | 'elemental_fire'
  | 'realm_shift'
  | 'chrono_sync';

export interface FluxEvent {
  type: FluxEventType;
  name: string;
  description: string;
  turnsRemaining: number;
}

export type EvolvedPieceType =
  | 'archon'        // Pawn evolution: moves like Knight + Bishop
  | 'phantom_knight' // Knight evolution: can move through pieces
  | 'sniper_bishop'  // Bishop evolution: captures from any distance
  | 'royal_guard';   // Rook evolution: can move one square diagonally

export interface PieceEvolution {
  square: Square;
  originalType: PieceSymbol;
  evolvedType: EvolvedPieceType;
  color: Color;
}

export interface PieceExperience {
  square: Square;
  type: PieceSymbol;
  color: Color;
  moveCount: number;
  captureCount: number;
  forksPerformed: number; // For Knight evolution
  knightsCaptured: number; // For Bishop evolution
  hasCastled: boolean; // For Rook evolution
}

export interface GameState {
  turnCount: number;
  activeFlux: FluxEvent | null;
  nextFluxTurn: number;
  pieceEvolutions: Map<Square, PieceEvolution>;
  pieceExperience: Map<Square, PieceExperience>;
  gravityWellActive: boolean;
  anarchyModeActive: boolean;
}

export interface FluxDiceRoll {
  result: FluxEventType;
  animation: boolean;
}
