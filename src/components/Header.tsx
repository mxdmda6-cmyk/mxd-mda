// components/Header.tsx

import React from 'react';

export const Header = () => {
  return (
    <header className="bg-brand-surface p-4 border-b border-gray-800">
      <div className="container mx-auto">
        <h1 className="text-2xl font-black text-brand-text tracking-tighter">
          YouTube Automation System — <span className="text-brand-secondary">MXD-MDA</span>
        </h1>
        <p className="font-mono text-sm text-brand-text-dim">Your AI-Powered Content Machine</p>
      </div>
    </header>
  );
};