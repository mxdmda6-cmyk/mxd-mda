// components/CreativeAssistantModal.tsx

import React, { useState } from 'react';
import { generateContent } from '../services/geminiService';

interface CreativeAssistantModalProps {
  isOpen: boolean;
  onClose: () => void;
  onIdeaGenerated: (prompt: string, title: string, script: string) => void;
}

export const CreativeAssistantModal: React.FC<CreativeAssistantModalProps> = ({ isOpen, onClose, onIdeaGenerated }) => {
  const [prompt, setPrompt] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async () => {
    if (!prompt) return;
    setIsLoading(true);
    setError(null);
    try {
      const { title, script } = await generateContent(prompt);
      if (title && script) {
        onIdeaGenerated(prompt, title, script);
        setPrompt('');
        onClose();
      }
    } catch (err) {
      setError('Failed to generate content. Please check the console for details.');
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50">
      <div className="bg-brand-surface p-8 rounded-lg shadow-2xl w-full max-w-2xl border border-gray-700">
        <h2 className="text-2xl font-bold mb-4 text-brand-text">Creative Assistant</h2>
        <p className="text-brand-text-dim mb-6">Describe your video idea, and the AI will generate a title and script.</p>
        <textarea
          className="w-full p-3 bg-brand-bg border border-gray-600 rounded-lg text-brand-text focus:ring-2 focus:ring-brand-primary focus:outline-none"
          rows={4}
          placeholder="e.g., A 1-minute video about the history of retro synthesizers"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
        {error && <p className="text-red-500 mt-2">{error}</p>}
        <div className="flex justify-end gap-4 mt-6">
          <button onClick={onClose} className="py-2 px-5 bg-gray-600 hover:bg-gray-700 rounded-lg text-white font-semibold transition-colors">
            Cancel
          </button>
          <button onClick={handleSubmit} disabled={isLoading} className="py-2 px-5 bg-brand-primary hover:bg-blue-500 rounded-lg text-white font-semibold disabled:bg-gray-500 transition-colors">
            {isLoading ? 'Generating...' : 'Generate Idea'}
          </button>
        </div>
      </div>
    </div>
  );
};