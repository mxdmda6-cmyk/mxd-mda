import { Chess, Square, Move, PieceSymbol, Color } from 'chess.js';
import {
  GameState,
  FluxEvent,
  PieceEvolution,
  PieceExperience,
  EvolvedPieceType,
} from './types';
import {
  rollFluxEvent,
  createFluxEvent,
  getGravityWellVictims,
  isAnarchyMoveValid,
  getFireSplashTargets,
} from './fluxEvents';
import { isKnightMove, isDiagonal } from './chessUtils';

const FLUX_INTERVAL = 5; // Flux happens every 5 turns

export class QuantumChess {
  private game: Chess;
  private state: GameState;

  constructor() {
    this.game = new Chess();
    this.state = {
      turnCount: 0,
      activeFlux: null,
      nextFluxTurn: FLUX_INTERVAL,
      pieceEvolutions: new Map(),
      pieceExperience: new Map(),
      gravityWellActive: false,
      anarchyModeActive: false,
    };
  }

  /**
   * Get the current chess.js instance
   */
  getGame(): Chess {
    return this.game;
  }

  /**
   * Get the current game state
   */
  getState(): GameState {
    return this.state;
  }

  /**
   * Initialize piece experience for all pieces on the board
   */
  private initializePieceExperience() {
    const board = this.game.board();

    for (let rank = 0; rank < 8; rank++) {
      for (let file = 0; file < 8; file++) {
        const piece = board[rank][file];
        if (piece) {
          const square = `${String.fromCharCode(97 + file)}${rank + 1}` as Square;
          if (!this.state.pieceExperience.has(square)) {
            this.state.pieceExperience.set(square, {
              square,
              type: piece.type,
              color: piece.color,
              moveCount: 0,
              captureCount: 0,
              forksPerformed: 0,
              knightsCaptured: 0,
              hasCastled: false,
            });
          }
        }
      }
    }
  }

  /**
   * Make a move with Flux and evolution logic
   */
  move(from: Square, to: Square): Move | null {
    // Validate move based on current flux
    if (!this.isValidQuantumMove(from, to)) {
      return null;
    }

    // Check for evolution conditions
    const piece = this.game.get(from);
    if (!piece) return null;

    // Make the standard move
    const move = this.game.move({ from, to });
    if (!move) return null;

    // Update piece experience
    this.updatePieceExperience(move);

    // Handle Flux effects after move
    this.applyFluxEffects(move);

    // Check for evolution triggers
    this.checkEvolutionTriggers(move);

    // Increment turn counter
    this.state.turnCount++;

    // Check for Quantum Flux trigger
    if (this.state.turnCount >= this.state.nextFluxTurn) {
      this.triggerQuantumFlux();
    }

    // Update active flux duration
    if (this.state.activeFlux) {
      this.state.activeFlux.turnsRemaining--;
      if (this.state.activeFlux.turnsRemaining <= 0) {
        this.deactivateFlux();
      }
    }

    // Apply Gravity Well destruction
    if (this.state.gravityWellActive) {
      this.applyGravityWell();
    }

    return move;
  }

  /**
   * Validate move based on active flux events and evolutions
   */
  private isValidQuantumMove(from: Square, to: Square): boolean {
    const piece = this.game.get(from);
    if (!piece) return false;

    // Check if piece has evolved
    const evolution = this.state.pieceEvolutions.get(from);
    if (evolution) {
      return this.isEvolvedMoveValid(from, to, evolution);
    }

    // Anarchy mode: all pieces move like queens
    if (this.state.anarchyModeActive) {
      return isAnarchyMoveValid(from, to);
    }

    // Standard chess validation
    const moves = this.game.moves({ square: from, verbose: true });
    return moves.some(m => m.to === to);
  }

  /**
   * Validate move for evolved pieces
   */
  private isEvolvedMoveValid(from: Square, to: Square, evolution: PieceEvolution): boolean {
    switch (evolution.evolvedType) {
      case 'archon':
        // Moves like Knight + Bishop
        return isKnightMove(from, to) || isDiagonal(from, to);

      case 'phantom_knight':
        // Can move through pieces
        return isKnightMove(from, to);

      case 'sniper_bishop':
        // Can capture from any distance on diagonal
        return isDiagonal(from, to);

      case 'royal_guard':
        // Rook + one diagonal move
        const standardMoves = this.game.moves({ square: from, verbose: true });
        const isStandardValid = standardMoves.some(m => m.to === to);
        const isDiagonalAdjacent = isDiagonal(from, to) &&
          Math.abs(from.charCodeAt(0) - to.charCodeAt(0)) === 1;
        return isStandardValid || isDiagonalAdjacent;

      default:
        return false;
    }
  }

  /**
   * Update piece experience after a move
   */
  private updatePieceExperience(move: Move) {
    const exp = this.state.pieceExperience.get(move.from as Square);
    if (exp) {
      exp.moveCount++;
      if (move.captured) {
        exp.captureCount++;
      }
      // Update the experience at the new square
      this.state.pieceExperience.delete(move.from as Square);
      exp.square = move.to as Square;
      this.state.pieceExperience.set(move.to as Square, exp);
    }
  }

  /**
   * Apply flux effects after a move
   */
  private applyFluxEffects(move: Move) {
    if (!this.state.activeFlux) return;

    switch (this.state.activeFlux.type) {
      case 'elemental_fire':
        if (move.captured) {
          this.applyFireDamage(move.to as Square);
        }
        break;

      // Other flux effects handled elsewhere
    }
  }

  /**
   * Apply fire splash damage to adjacent squares
   */
  private applyFireDamage(captureSquare: Square) {
    const targets = getFireSplashTargets(captureSquare);

    // In real implementation, would remove pieces from board
    // For now, just log the damage
    targets.forEach(target => {
      const piece = this.game.get(target);
      if (piece) {
        console.log(`🔥 Fire damage: ${piece.type} on ${target}`);
        // Note: chess.js doesn't have a method to remove arbitrary pieces
        // In a full implementation, we'd need to modify the board state directly
      }
    });
  }

  /**
   * Check if any pieces should evolve
   */
  private checkEvolutionTriggers(move: Move) {
    const exp = this.state.pieceExperience.get(move.to as Square);
    if (!exp) return;

    const piece = this.game.get(move.to as Square);
    if (!piece) return;

    // Pawn → Archon (reached back rank)
    if (piece.type === 'p') {
      const backRank = piece.color === 'w' ? '8' : '1';
      if (move.to[1] === backRank) {
        this.evolvePiece(move.to as Square, 'archon');
      }
    }

    // Knight → Phantom Knight (3 forks)
    if (piece.type === 'n' && exp.forksPerformed >= 3) {
      this.evolvePiece(move.to as Square, 'phantom_knight');
    }

    // Bishop → Sniper Bishop (captured both opponent knights)
    if (piece.type === 'b' && exp.knightsCaptured >= 2) {
      this.evolvePiece(move.to as Square, 'sniper_bishop');
    }

    // Rook → Royal Guard (after castling)
    if (piece.type === 'r' && exp.hasCastled) {
      this.evolvePiece(move.to as Square, 'royal_guard');
    }
  }

  /**
   * Evolve a piece to its new form
   */
  private evolvePiece(square: Square, evolvedType: EvolvedPieceType) {
    const piece = this.game.get(square);
    if (!piece) return;

    const evolution: PieceEvolution = {
      square,
      originalType: piece.type,
      evolvedType,
      color: piece.color,
    };

    this.state.pieceEvolutions.set(square, evolution);
    console.log(`✨ Evolution: ${piece.type} → ${evolvedType} at ${square}`);
  }

  /**
   * Trigger a Quantum Flux event
   */
  private triggerQuantumFlux() {
    const fluxType = rollFluxEvent();
    this.state.activeFlux = createFluxEvent(fluxType);
    this.state.nextFluxTurn = this.state.turnCount + FLUX_INTERVAL;

    // Activate special flux states
    this.state.gravityWellActive = fluxType === 'gravity_well';
    this.state.anarchyModeActive = fluxType === 'anarchy_mode';

    console.log(`⚡ QUANTUM FLUX: ${this.state.activeFlux.name}`);
  }

  /**
   * Deactivate current flux
   */
  private deactivateFlux() {
    console.log(`✓ Flux ended: ${this.state.activeFlux?.name}`);
    this.state.activeFlux = null;
    this.state.gravityWellActive = false;
    this.state.anarchyModeActive = false;
  }

  /**
   * Apply Gravity Well destruction
   */
  private applyGravityWell() {
    const victims = getGravityWellVictims(this.game);
    if (victims.length > 0) {
      console.log(`🌀 Gravity Well claims: ${victims.join(', ')}`);
      // Note: Would need to remove pieces from board
    }
  }

  /**
   * Get all valid moves for the current position
   */
  moves(options?: { square?: Square }): Move[] {
    return this.game.moves({ ...options, verbose: true });
  }

  /**
   * Check if game is over
   */
  isGameOver(): boolean {
    return this.game.isGameOver();
  }

  /**
   * Check if current player is in check
   */
  inCheck(): boolean {
    return this.game.inCheck();
  }

  /**
   * Get current turn
   */
  turn(): Color {
    return this.game.turn();
  }

  /**
   * Get FEN string
   */
  fen(): string {
    return this.game.fen();
  }

  /**
   * Reset the game
   */
  reset() {
    this.game.reset();
    this.state = {
      turnCount: 0,
      activeFlux: null,
      nextFluxTurn: FLUX_INTERVAL,
      pieceEvolutions: new Map(),
      pieceExperience: new Map(),
      gravityWellActive: false,
      anarchyModeActive: false,
    };
    this.initializePieceExperience();
  }
}
