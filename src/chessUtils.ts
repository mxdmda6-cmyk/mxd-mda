/**
 * Chess Move Utilities
 *
 * A collection of utility functions for chess move validation and analysis.
 * Squares are represented in algebraic notation (e.g., "e4", "a1", "h8").
 */

/**
 * Checks if two squares are on the same file (column).
 * @param a - First square in algebraic notation
 * @param b - Second square in algebraic notation
 * @returns true if both squares are on the same file
 */
export function isSameFile(a: string, b: string): boolean {
  return a[0] === b[0];
}

/**
 * Checks if two squares are on the same rank (row).
 * @param a - First square in algebraic notation
 * @param b - Second square in algebraic notation
 * @returns true if both squares are on the same rank
 */
export function isSameRank(a: string, b: string): boolean {
  return a[1] === b[1];
}

/**
 * Returns the file index (0-7) for a given square.
 * @param sq - Square in algebraic notation
 * @returns File index (0=a, 1=b, ..., 7=h)
 */
export function fileIndex(sq: string): number {
  return 'abcdefgh'.indexOf(sq[0]);
}

/**
 * Returns the rank index (0-7) for a given square.
 * @param sq - Square in algebraic notation
 * @returns Rank index (0=1, 1=2, ..., 7=8)
 */
export function rankIndex(sq: string): number {
  return parseInt(sq[1], 10) - 1;
}

/**
 * Checks if two squares are on the same diagonal.
 * @param a - First square in algebraic notation
 * @param b - Second square in algebraic notation
 * @returns true if both squares are on the same diagonal
 */
export function isDiagonal(a: string, b: string): boolean {
  return Math.abs(fileIndex(a) - fileIndex(b)) === Math.abs(rankIndex(a) - rankIndex(b));
}

/**
 * Checks if a move from square a to square b is a valid queen move.
 * Queens can move horizontally, vertically, or diagonally.
 * @param a - Starting square in algebraic notation
 * @param b - Target square in algebraic notation
 * @returns true if the move is a valid queen move pattern
 */
export function isQueenMove(a: string, b: string): boolean {
  return isSameFile(a, b) || isSameRank(a, b) || isDiagonal(a, b);
}

/**
 * Checks if a move from square a to square b is a valid knight move.
 * Knights move in an L-shape: 2 squares in one direction and 1 in the perpendicular direction.
 * @param a - Starting square in algebraic notation
 * @param b - Target square in algebraic notation
 * @returns true if the move is a valid knight move pattern
 */
export function isKnightMove(a: string, b: string): boolean {
  const df = Math.abs(fileIndex(a) - fileIndex(b));
  const dr = Math.abs(rankIndex(a) - rankIndex(b));
  return (df === 1 && dr === 2) || (df === 2 && dr === 1);
}

/**
 * Returns an array of squares that lie strictly between two squares along a straight or diagonal ray.
 * Returns an empty array if the squares are not aligned or are adjacent.
 * @param a - Starting square in algebraic notation
 * @param b - Ending square in algebraic notation
 * @returns Array of squares between a and b (excluding a and b themselves)
 */
export function rayBetween(a: string, b: string): string[] {
  // squares strictly between a and b along straight or diagonal rays
  const af = fileIndex(a);
  const ar = rankIndex(a);
  const bf = fileIndex(b);
  const br = rankIndex(b);
  const df = Math.sign(bf - af);
  const dr = Math.sign(br - ar);
  const steps = Math.max(Math.abs(bf - af), Math.abs(br - ar));
  const out: string[] = [];
  for (let i = 1; i < steps; i++) {
    const f = af + df * i;
    const r = ar + dr * i;
    out.push('abcdefgh'[f] + (r + 1));
  }
  return out;
}
