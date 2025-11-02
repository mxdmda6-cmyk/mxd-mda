import { Chess, Square, Move } from 'chess.js';
import { FluxEvent, FluxEventType } from './types';
import { isDiagonal, isKnightMove, rayBetween } from './chessUtils';

const GRAVITY_WELL_SQUARES: Square[] = ['d4', 'd5', 'e4', 'e5'];

export const FLUX_EVENTS: Record<FluxEventType, Omit<FluxEvent, 'turnsRemaining'>> = {
  gravity_well: {
    type: 'gravity_well',
    name: 'GRAVITY WELL',
    description: 'Center 4 squares (d4-e5) pull in adjacent pieces and destroy them!',
  },
  anarchy_mode: {
    type: 'anarchy_mode',
    name: 'ANARCHY MODE',
    description: 'All pieces move like Queens for 1 turn (can only capture once)!',
  },
  elemental_fire: {
    type: 'elemental_fire',
    name: 'ELEMENTAL: FIRE',
    description: 'Captures cause splash damage to adjacent pieces!',
  },
  realm_shift: {
    type: 'realm_shift',
    name: 'REALM SHIFT',
    description: 'Board splits: Left=Standard, Right=Modified rules!',
  },
  chrono_sync: {
    type: 'chrono_sync',
    name: 'CHRONO-SYNC',
    description: 'Unmoved pieces can teleport 1 square!',
  },
};

export function rollFluxEvent(): FluxEventType {
  const events: FluxEventType[] = [
    'gravity_well',
    'anarchy_mode',
    'elemental_fire',
    'realm_shift',
    'chrono_sync',
  ];
  return events[Math.floor(Math.random() * events.length)];
}

export function createFluxEvent(type: FluxEventType, duration: number = 5): FluxEvent {
  return {
    ...FLUX_EVENTS[type],
    turnsRemaining: duration,
  };
}

/**
 * Gravity Well: Checks if a piece is adjacent to the center vortex
 */
export function isAdjacentToGravityWell(square: Square): boolean {
  const file = square.charCodeAt(0);
  const rank = parseInt(square[1]);

  for (const wellSquare of GRAVITY_WELL_SQUARES) {
    const wellFile = wellSquare.charCodeAt(0);
    const wellRank = parseInt(wellSquare[1]);

    const fileDiff = Math.abs(file - wellFile);
    const rankDiff = Math.abs(rank - wellRank);

    if ((fileDiff === 1 && rankDiff === 0) ||
        (fileDiff === 0 && rankDiff === 1) ||
        (fileDiff === 1 && rankDiff === 1)) {
      return true;
    }
  }
  return false;
}

/**
 * Gravity Well: Gets all squares that should be destroyed
 */
export function getGravityWellVictims(game: Chess): Square[] {
  const victims: Square[] = [];
  const board = game.board();

  for (let rank = 0; rank < 8; rank++) {
    for (let file = 0; file < 8; file++) {
      const piece = board[rank][file];
      if (piece) {
        const square = `${String.fromCharCode(97 + file)}${rank + 1}` as Square;
        if (isAdjacentToGravityWell(square)) {
          victims.push(square);
        }
      }
    }
  }

  return victims;
}

/**
 * Anarchy Mode: Validates if move follows Queen movement pattern
 */
export function isAnarchyMoveValid(from: Square, to: Square): boolean {
  // In anarchy mode, all pieces can move like queens
  return isDiagonal(from, to) ||
         from[0] === to[0] || // same file (vertical)
         from[1] === to[1];   // same rank (horizontal)
}

/**
 * Elemental Fire: Gets squares affected by splash damage
 */
export function getFireSplashTargets(captureSquare: Square): Square[] {
  const targets: Square[] = [];
  const file = captureSquare.charCodeAt(0);
  const rank = parseInt(captureSquare[1]);

  // All 8 adjacent squares
  for (let df = -1; df <= 1; df++) {
    for (let dr = -1; dr <= 1; dr++) {
      if (df === 0 && dr === 0) continue; // Skip the capture square itself

      const newFile = file + df;
      const newRank = rank + dr;

      if (newFile >= 97 && newFile <= 104 && newRank >= 1 && newRank <= 8) {
        targets.push(`${String.fromCharCode(newFile)}${newRank}` as Square);
      }
    }
  }

  return targets;
}

/**
 * Realm Shift: Checks if a square is on the left or right side
 */
export function getRealm(square: Square): 'left' | 'right' {
  const file = square.charCodeAt(0);
  return file <= 100 ? 'left' : 'right'; // a-d = left, e-h = right
}

/**
 * Chrono-Sync: Checks if a piece can teleport (hasn't moved)
 */
export function canTeleport(moveCount: number): boolean {
  return moveCount === 0;
}

/**
 * Chrono-Sync: Gets valid teleport destinations (1 square in any direction)
 */
export function getTeleportDestinations(square: Square): Square[] {
  const destinations: Square[] = [];
  const file = square.charCodeAt(0);
  const rank = parseInt(square[1]);

  for (let df = -1; df <= 1; df++) {
    for (let dr = -1; dr <= 1; dr++) {
      if (df === 0 && dr === 0) continue;

      const newFile = file + df;
      const newRank = rank + dr;

      if (newFile >= 97 && newFile <= 104 && newRank >= 1 && newRank <= 8) {
        destinations.push(`${String.fromCharCode(newFile)}${newRank}` as Square);
      }
    }
  }

  return destinations;
}
