/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // NES-era color palette
        'nes-dark': '#0f380f',
        'nes-light': '#8bac0f',
        'nes-accent': '#306230',
        'nes-bright': '#9bbc0f',
        'flux-blue': '#00ffff',
        'flux-purple': '#ff00ff',
        'evolution-gold': '#ffb000',
        'pixel-red': '#ff0000',
        'pixel-white': '#ffffff',
      },
      fontFamily: {
        'pixel': ['"Press Start 2P"', 'monospace'],
        'game': ['"Space Grotesk"', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
