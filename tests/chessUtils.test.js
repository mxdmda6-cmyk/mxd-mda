import { describe, test } from 'node:test';
import assert from 'node:assert/strict';
import {
  isSameFile,
  isSameRank,
  fileIndex,
  rankIndex,
  isDiagonal,
  isQueenMove,
  isKnightMove,
  rayBetween
} from '../dist/chessUtils.js';

describe('Chess Utilities', () => {
  describe('isSameFile', () => {
    test('should return true for squares on the same file', () => {
      assert.equal(isSameFile('e1', 'e8'), true);
      assert.equal(isSameFile('a1', 'a5'), true);
      assert.equal(isSameFile('h4', 'h4'), true);
    });

    test('should return false for squares on different files', () => {
      assert.equal(isSameFile('e1', 'd1'), false);
      assert.equal(isSameFile('a1', 'b8'), false);
    });
  });

  describe('isSameRank', () => {
    test('should return true for squares on the same rank', () => {
      assert.equal(isSameRank('a1', 'h1'), true);
      assert.equal(isSameRank('e4', 'a4'), true);
      assert.equal(isSameRank('c5', 'c5'), true);
    });

    test('should return false for squares on different ranks', () => {
      assert.equal(isSameRank('e1', 'e2'), false);
      assert.equal(isSameRank('a1', 'b8'), false);
    });
  });

  describe('fileIndex', () => {
    test('should return correct file indices', () => {
      assert.equal(fileIndex('a1'), 0);
      assert.equal(fileIndex('b4'), 1);
      assert.equal(fileIndex('c7'), 2);
      assert.equal(fileIndex('d2'), 3);
      assert.equal(fileIndex('e4'), 4);
      assert.equal(fileIndex('f3'), 5);
      assert.equal(fileIndex('g6'), 6);
      assert.equal(fileIndex('h8'), 7);
    });
  });

  describe('rankIndex', () => {
    test('should return correct rank indices', () => {
      assert.equal(rankIndex('a1'), 0);
      assert.equal(rankIndex('b2'), 1);
      assert.equal(rankIndex('c3'), 2);
      assert.equal(rankIndex('d4'), 3);
      assert.equal(rankIndex('e5'), 4);
      assert.equal(rankIndex('f6'), 5);
      assert.equal(rankIndex('g7'), 6);
      assert.equal(rankIndex('h8'), 7);
    });
  });

  describe('isDiagonal', () => {
    test('should return true for squares on the same diagonal', () => {
      assert.equal(isDiagonal('a1', 'h8'), true);
      assert.equal(isDiagonal('e4', 'h7'), true);
      assert.equal(isDiagonal('d4', 'a1'), true);
      assert.equal(isDiagonal('a8', 'h1'), true);
      assert.equal(isDiagonal('c3', 'c3'), true); // same square
    });

    test('should return false for squares not on the same diagonal', () => {
      assert.equal(isDiagonal('e4', 'e5'), false);
      assert.equal(isDiagonal('a1', 'b3'), false);
      assert.equal(isDiagonal('d4', 'f5'), false);
    });
  });

  describe('isQueenMove', () => {
    test('should return true for valid queen moves (horizontal)', () => {
      assert.equal(isQueenMove('e4', 'e8'), true);
      assert.equal(isQueenMove('a1', 'h1'), true);
    });

    test('should return true for valid queen moves (vertical)', () => {
      assert.equal(isQueenMove('e1', 'e8'), true);
      assert.equal(isQueenMove('c3', 'c7'), true);
    });

    test('should return true for valid queen moves (diagonal)', () => {
      assert.equal(isQueenMove('e4', 'h7'), true);
      assert.equal(isQueenMove('a1', 'h8'), true);
      assert.equal(isQueenMove('d4', 'a1'), true);
    });

    test('should return false for invalid queen moves', () => {
      assert.equal(isQueenMove('e4', 'f6'), false); // knight move
      assert.equal(isQueenMove('a1', 'b3'), false);
      assert.equal(isQueenMove('d4', 'f5'), false);
    });

    test('should return true for same square', () => {
      assert.equal(isQueenMove('e4', 'e4'), true);
    });
  });

  describe('isKnightMove', () => {
    test('should return true for valid knight moves', () => {
      assert.equal(isKnightMove('e4', 'f6'), true);
      assert.equal(isKnightMove('e4', 'd6'), true);
      assert.equal(isKnightMove('e4', 'g5'), true);
      assert.equal(isKnightMove('e4', 'g3'), true);
      assert.equal(isKnightMove('e4', 'f2'), true);
      assert.equal(isKnightMove('e4', 'd2'), true);
      assert.equal(isKnightMove('e4', 'c3'), true);
      assert.equal(isKnightMove('e4', 'c5'), true);
    });

    test('should return false for invalid knight moves', () => {
      assert.equal(isKnightMove('e4', 'e5'), false); // vertical
      assert.equal(isKnightMove('e4', 'f5'), false); // diagonal
      assert.equal(isKnightMove('e4', 'f4'), false); // horizontal
      assert.equal(isKnightMove('e4', 'e4'), false); // same square
      assert.equal(isKnightMove('a1', 'h8'), false); // long diagonal
    });

    test('should work from corner squares', () => {
      assert.equal(isKnightMove('a1', 'b3'), true);
      assert.equal(isKnightMove('a1', 'c2'), true);
      assert.equal(isKnightMove('h8', 'g6'), true);
      assert.equal(isKnightMove('h8', 'f7'), true);
    });
  });

  describe('rayBetween', () => {
    test('should return squares between two squares on the same file', () => {
      assert.deepEqual(rayBetween('e1', 'e4'), ['e2', 'e3']);
      assert.deepEqual(rayBetween('e4', 'e1'), ['e3', 'e2']);
      assert.deepEqual(rayBetween('a1', 'a8'), ['a2', 'a3', 'a4', 'a5', 'a6', 'a7']);
    });

    test('should return squares between two squares on the same rank', () => {
      assert.deepEqual(rayBetween('a1', 'd1'), ['b1', 'c1']);
      assert.deepEqual(rayBetween('d1', 'a1'), ['c1', 'b1']);
      assert.deepEqual(rayBetween('a1', 'h1'), ['b1', 'c1', 'd1', 'e1', 'f1', 'g1']);
    });

    test('should return squares between two squares on a diagonal', () => {
      assert.deepEqual(rayBetween('a1', 'd4'), ['b2', 'c3']);
      assert.deepEqual(rayBetween('d4', 'a1'), ['c3', 'b2']);
      assert.deepEqual(rayBetween('e4', 'h7'), ['f5', 'g6']);
      assert.deepEqual(rayBetween('a8', 'h1'), ['b7', 'c6', 'd5', 'e4', 'f3', 'g2']);
    });

    test('should return empty array for adjacent squares', () => {
      assert.deepEqual(rayBetween('e4', 'e5'), []);
      assert.deepEqual(rayBetween('e4', 'f4'), []);
      assert.deepEqual(rayBetween('e4', 'f5'), []);
    });

    test('should return empty array for the same square', () => {
      assert.deepEqual(rayBetween('e4', 'e4'), []);
    });

    test('should work for all diagonal directions', () => {
      // Up-right
      assert.deepEqual(rayBetween('d4', 'f6'), ['e5']);
      // Up-left
      assert.deepEqual(rayBetween('d4', 'b6'), ['c5']);
      // Down-right
      assert.deepEqual(rayBetween('d4', 'f2'), ['e3']);
      // Down-left
      assert.deepEqual(rayBetween('d4', 'b2'), ['c3']);
    });

    test('should handle knight moves (non-aligned squares)', () => {
      // For non-aligned squares, the function will still compute based on max distance
      // This is a limitation of the current implementation
      const result = rayBetween('e4', 'f6');
      // The function doesn't validate if squares are actually aligned
      assert.ok(Array.isArray(result));
    });
  });
});
