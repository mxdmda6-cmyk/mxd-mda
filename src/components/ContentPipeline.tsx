// components/ContentPipeline.tsx

import React from 'react';
import { Video, VideoStatus } from '../types';
import { VideoCard } from './VideoCard';
import { PlusIcon } from './icons';

interface ContentPipelineProps {
  videos: Video[];
  onOpenCreativeAssistant: () => void;
  onOpenUploadModal: (video: Video) => void;
}

export const ContentPipeline: React.FC<ContentPipelineProps> = ({ videos, onOpenCreativeAssistant, onOpenUploadModal }) => {
  const columns: VideoStatus[] = [VideoStatus.Idea, VideoStatus.Scripting, VideoStatus.Scheduled, VideoStatus.Published];

  const getVideosByStatus = (status: VideoStatus) => {
    return videos.filter(video => video.status === status);
  };

  return (
    <div className="p-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        {columns.map(status => (
          <div key={status} className="bg-brand-bg rounded-lg p-4 border border-gray-800">
            <h2 className="text-xl font-black mb-6 text-center tracking-wider uppercase text-brand-text-dim">{status}</h2>

            {status === VideoStatus.Idea && (
              <button
                onClick={onOpenCreativeAssistant}
                className="w-full flex items-center justify-center gap-2 p-3 mb-4 bg-brand-primary/20 text-brand-primary rounded-lg border-2 border-dashed border-brand-primary/50 hover:bg-brand-primary/30 transition-all"
              >
                <PlusIcon />
                New Idea
              </button>
            )}

            <div className="space-y-4">
              {getVideosByStatus(status).map(video => (
                <VideoCard key={video.id} video={video} onUploadClick={onOpenUploadModal} />
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};