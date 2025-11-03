# 🎮 Quantum Gambit 8-Bit

![Quantum Gambit](https://img.shields.io/badge/chess-quantum-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?logo=typescript&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-black?logo=next.js&logoColor=white)

**Where Chess Meets Quantum Chaos** ⚡

An innovative chess game that combines classic strategy with dynamic "Quantum Flux" mechanics and piece evolution. Built with authentic 8-bit NES-era aesthetics and smooth modern gameplay.

## 🌟 Features

### ⚡ Quantum Flux Matrix
Every **5 turns**, the board undergoes a dramatic transformation:

- **🌀 Gravity Well**: Center squares (d4-e5) become a vortex that destroys adjacent pieces
- **👑 Anarchy Mode**: All pieces can move like Queens for one turn (1 capture only)
- **🔥 Elemental: Fire**: Captures cause splash damage to surrounding pieces
- **🔀 Realm Shift**: Board splits into left/right with different rule sets
- **⏰ Chrono-Sync**: Unmoved pieces gain teleport abilities

### ✨ Dynamic Piece Evolution
Pieces evolve based on their actions:

- **⚜ Archon** (Pawn): Reaches back rank → Moves like Knight + Bishop
- **⚔ Phantom Knight** (Knight): 3 fork attacks → Can move through pieces
- **🎯 Sniper Bishop** (Bishop): Captures both enemy knights → Long-range diagonal attacks
- **🛡 Royal Guard** (Rook): After castling → Gains diagonal movement

### 🎨 Authentic 8-Bit Aesthetic
- NES-era color palette (54 colors)
- Pixel-perfect rendering
- Smooth 60fps animations
- Scanline effects
- Retro sound design ready

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/quantum-gambit.git
cd quantum-gambit

# Install dependencies
npm install

# Run development server
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) to play!

### Production Build

```bash
npm run build
npm start
```

## 🎯 How to Play

1. **Standard Chess Rules Apply** - By default, play regular chess
2. **Watch the Flux Timer** - Track when the next Quantum Flux will trigger
3. **Adapt to Chaos** - When Flux activates, adapt your strategy to the new rules
4. **Evolve Your Pieces** - Perform special actions to unlock powerful evolutions
5. **Master the Quantum** - Use Flux events to your advantage!

## 🛠️ Technology Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Chess Engine**: chess.js
- **Styling**: Tailwind CSS
- **State Management**: React Hooks + Zustand (future)
- **Fonts**: Press Start 2P, Space Grotesk

## 📁 Project Structure

```
quantum-gambit/
├── app/
│   ├── page.tsx          # Main game page
│   ├── layout.tsx        # Root layout
│   └── globals.css       # Global styles & 8-bit theme
├── components/
│   ├── ChessBoard.tsx    # Main board component
│   ├── ChessSquare.tsx   # Individual square
│   ├── ChessPiece.tsx    # Piece renderer
│   ├── FluxIndicator.tsx # Flux event display
│   ├── GameInfo.tsx      # Turn & status info
│   └── EvolutionTracker.tsx # Track evolved pieces
├── lib/
│   ├── quantumChess.ts   # Core game engine
│   ├── fluxEvents.ts     # Flux mechanics
│   ├── chessUtils.ts     # Chess utility functions
│   └── types.ts          # TypeScript definitions
└── public/
    └── (assets)          # Images, sounds, etc.
```

## 🎮 Game Modes (Planned)

- ✅ **Flux Duel** - Standard game with Quantum Flux
- 🔲 **Quantum Campaign** - Story mode introducing mechanics
- 🔲 **Pixel Puzzle Mode** - Chess puzzles using Flux events
- 🔲 **The Gauntlet** - Face AI with different Flux specialties
- 🔲 **Online Multiplayer** - Play against others online
- 🔲 **Codex Builder** - Create custom Flux events

## 🧪 Development

### Chess Utilities
The game uses custom chess utility functions for:
- Move validation (`isQueenMove`, `isKnightMove`)
- Square analysis (`isSameFile`, `isDiagonal`)
- Ray calculations (`rayBetween`)

### Adding New Flux Events
1. Define event in `lib/types.ts`
2. Implement logic in `lib/fluxEvents.ts`
3. Add validation in `lib/quantumChess.ts`
4. Update UI in components

### Testing

```bash
# Run tests (when implemented)
npm test

# Type checking
npx tsc --noEmit
```

## 🎨 Design Philosophy

**MXD (Mixed)**: Dynamic mixing of game elements through Quantum Flux
**MDA (Model-Driven Architecture)**: Flexible rule system driven by data models
**8-Bit Authenticity**: True to NES-era limitations while leveraging modern tech

## 🤝 Contributing

Contributions welcome! Areas of interest:
- Additional Flux events
- Sound effects & music
- AI opponents
- Multiplayer support
- Mobile optimization

## 📝 License

MIT License - Feel free to fork and create your own quantum chess variants!

## 🙏 Credits

- Chess logic powered by [chess.js](https://github.com/jhlywa/chess.js)
- Inspired by classic NES games and modern roguelikes
- Built with love for chess and retro gaming

## 🎯 Roadmap

- [x] Core chess engine with Flux Matrix
- [x] Piece evolution system
- [x] 8-bit UI with animations
- [ ] Sound effects and chiptune music
- [ ] Campaign mode
- [ ] Pixel Puzzle challenges
- [ ] Online multiplayer
- [ ] Custom Flux event builder
- [ ] Mobile app version

---

**Made with ⚡ quantum energy and 💚 pixel love**

*Que viva la estrategia! 🎮♟️*
