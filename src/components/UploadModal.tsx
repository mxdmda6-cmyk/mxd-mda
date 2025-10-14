// components/UploadModal.tsx

import React, { useState } from 'react';
import { Video } from '../types';

interface UploadModalProps {
  video: Video | null;
  isOpen: boolean;
  onClose: () => void;
  onUpload: (video: Video, videoFile: File) => void;
}

export const UploadModal: React.FC<UploadModalProps> = ({ video, isOpen, onClose, onUpload }) => {
  const [videoFile, setVideoFile] = useState<File | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setVideoFile(event.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!video || !videoFile) return;
    setIsLoading(true);
    // In a real app, you would call the backend service here.
    // For now, we simulate the call.
    await onUpload(video, videoFile);
    setIsLoading(false);
    onClose();
  };

  if (!isOpen || !video) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50">
      <div className="bg-brand-surface p-8 rounded-lg shadow-2xl w-full max-w-2xl border border-gray-700">
        <h2 className="text-2xl font-bold mb-2 text-brand-text">Upload to YouTube</h2>
        <p className="text-brand-text-dim mb-6">Finalize details and upload your video.</p>

        <div className="mb-4">
          <label className="block text-brand-text-dim font-bold mb-2">Title</label>
          <input type="text" value={video.title} readOnly className="w-full p-3 bg-brand-bg border border-gray-600 rounded-lg text-brand-text-dim" />
        </div>

        <div className="mb-4">
          <label className="block text-brand-text-dim font-bold mb-2">Description / Script</label>
          <textarea value={video.script} readOnly rows={8} className="w-full p-3 bg-brand-bg border border-gray-600 rounded-lg text-brand-text-dim" />
        </div>

        <div className="mb-6">
          <label className="block text-brand-text-dim font-bold mb-2">Video File</label>
          <input type="file" accept="video/*" onChange={handleFileChange} className="w-full text-brand-text file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-brand-primary file:text-white hover:file:bg-blue-500" />
        </div>

        <div className="flex justify-end gap-4 mt-6">
          <button onClick={onClose} className="py-2 px-5 bg-gray-600 hover:bg-gray-700 rounded-lg text-white font-semibold transition-colors">
            Cancel
          </button>
          <button onClick={handleUpload} disabled={!videoFile || isLoading} className="py-2 px-5 bg-green-600 hover:bg-green-700 rounded-lg text-white font-semibold disabled:bg-gray-500 transition-colors">
            {isLoading ? 'Uploading...' : 'Upload Now'}
          </button>
        </div>
      </div>
    </div>
  );
};