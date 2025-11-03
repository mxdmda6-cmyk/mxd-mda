# Chess Move Utilities

A TypeScript library providing utility functions for chess move validation and analysis.

## Features

- **Square Comparison**: Check if squares share the same file or rank
- **Index Conversion**: Convert algebraic notation to numeric indices
- **Move Validation**: Validate queen and knight move patterns
- **Ray Analysis**: Find squares between two positions on a ray

## Installation

```bash
npm install
npm run build
```

## Usage

```typescript
import {
  isSameFile,
  isSameRank,
  fileIndex,
  rankIndex,
  isDiagonal,
  isQueenMove,
  isKnightMove,
  rayBetween
} from './dist/chessUtils.js';

// Check if squares are on the same file
isSameFile('e4', 'e8'); // true

// Validate a queen move
isQueenMove('d1', 'd8'); // true (vertical)
isQueenMove('a1', 'h8'); // true (diagonal)
isQueenMove('e4', 'f6'); // false (not a queen move)

// Validate a knight move
isKnightMove('e4', 'f6'); // true
isKnightMove('e4', 'e5'); // false

// Find squares between two positions
rayBetween('a1', 'a8'); // ['a2', 'a3', 'a4', 'a5', 'a6', 'a7']
rayBetween('e4', 'e6'); // ['e5']
```

## API Reference

### `isSameFile(a: string, b: string): boolean`
Checks if two squares are on the same file (column).

**Parameters:**
- `a`: First square in algebraic notation (e.g., "e4")
- `b`: Second square in algebraic notation

**Returns:** `true` if both squares are on the same file

---

### `isSameRank(a: string, b: string): boolean`
Checks if two squares are on the same rank (row).

**Parameters:**
- `a`: First square in algebraic notation
- `b`: Second square in algebraic notation

**Returns:** `true` if both squares are on the same rank

---

### `fileIndex(sq: string): number`
Returns the file index (0-7) for a given square.

**Parameters:**
- `sq`: Square in algebraic notation

**Returns:** File index (0=a, 1=b, ..., 7=h)

---

### `rankIndex(sq: string): number`
Returns the rank index (0-7) for a given square.

**Parameters:**
- `sq`: Square in algebraic notation

**Returns:** Rank index (0=1, 1=2, ..., 7=8)

---

### `isDiagonal(a: string, b: string): boolean`
Checks if two squares are on the same diagonal.

**Parameters:**
- `a`: First square in algebraic notation
- `b`: Second square in algebraic notation

**Returns:** `true` if both squares are on the same diagonal

---

### `isQueenMove(a: string, b: string): boolean`
Checks if a move from square a to square b is a valid queen move pattern. Queens can move horizontally, vertically, or diagonally.

**Parameters:**
- `a`: Starting square in algebraic notation
- `b`: Target square in algebraic notation

**Returns:** `true` if the move is a valid queen move pattern

**Note:** This function only validates the move pattern, not whether the path is clear or if the move is legal in the current game state.

---

### `isKnightMove(a: string, b: string): boolean`
Checks if a move from square a to square b is a valid knight move. Knights move in an L-shape: 2 squares in one direction and 1 in the perpendicular direction.

**Parameters:**
- `a`: Starting square in algebraic notation
- `b`: Target square in algebraic notation

**Returns:** `true` if the move is a valid knight move pattern

---

### `rayBetween(a: string, b: string): string[]`
Returns an array of squares that lie strictly between two squares along a straight or diagonal ray.

**Parameters:**
- `a`: Starting square in algebraic notation
- `b`: Ending square in algebraic notation

**Returns:** Array of squares between a and b (excluding a and b themselves)

**Examples:**
```typescript
rayBetween('a1', 'a4'); // ['a2', 'a3']
rayBetween('e4', 'h7'); // ['f5', 'g6']
rayBetween('e4', 'e5'); // [] (adjacent squares)
```

## Testing

Run the test suite:

```bash
npm test
```

Run tests in watch mode:

```bash
npm run test:watch
```

All tests are located in `/tests/chessUtils.test.js` with comprehensive coverage of:
- Edge cases (corner squares, same square)
- All move directions (vertical, horizontal, diagonal)
- Invalid moves
- Ray calculations in all directions

## Development

1. Make changes to `src/chessUtils.ts`
2. Build the TypeScript: `npm run build`
3. Run tests: `npm test`

## License

MIT
