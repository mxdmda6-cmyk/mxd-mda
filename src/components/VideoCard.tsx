// components/VideoCard.tsx

import React from 'react';
import { Video } from '../types';
import { UploadIcon } from './icons';

interface VideoCardProps {
  video: Video;
  onUploadClick: (video: Video) => void;
}

export const VideoCard: React.FC<VideoCardProps> = ({ video, onUploadClick }) => {
  return (
    <div className="bg-brand-surface p-4 rounded-lg shadow-md mb-4 border border-gray-700 hover:border-brand-primary transition-all">
      <h3 className="font-bold text-brand-text mb-2">{video.title}</h3>
      <p className="text-sm text-brand-text-dim line-clamp-3">{video.script}</p>
      {video.status === 'Scripting' && (
         <button
            onClick={() => onUploadClick(video)}
            className="mt-4 w-full bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg flex items-center justify-center transition-colors"
          >
           <UploadIcon />
           Ready to Upload
         </button>
      )}
      {video.youtubeUrl && (
        <a href={video.youtubeUrl} target="_blank" rel="noopener noreferrer" className="text-brand-primary mt-2 block truncate">
          {video.youtubeUrl}
        </a>
      )}
    </div>
  );
};