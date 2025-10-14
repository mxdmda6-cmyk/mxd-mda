// App.tsx

import React, { useState, useEffect } from 'react';
import { Header } from './components/Header';
import { login, onAuth } from './firebase';
import { ContentPipeline } from './components/ContentPipeline';
import { CreativeAssistantModal } from './components/CreativeAssistantModal';
import { UploadModal } from './components/UploadModal';
import { Video, VideoStatus } from './types';

function App() {
  const [videos, setVideos] = useState<Video[]>([
    // Some initial mock data
    { id: '1', title: 'The Lost Art of Mixtapes', prompt: '', script: 'A deep dive into the culture of creating mixtapes...', status: VideoStatus.Idea },
    { id: '2', title: 'Unboxing a 1985 Macintosh', prompt: '', script: 'Today, we unbox a piece of history...', status: VideoStatus.Scripting },
  ]);

  const [isCreativeAssistantOpen, setCreativeAssistantOpen] = useState(false);
  const [isUploadModalOpen, setUploadModalOpen] = useState(false);
  const [selectedVideo, setSelectedVideo] = useState<Video | null>(null);

  useEffect(() => {
    login();
    onAuth(user => {
      if (user) {
        console.log("User is signed in:", user.uid);
      } else {
        console.log("User is signed out.");
      }
    });
  }, []);

  const handleIdeaGenerated = (prompt: string, title: string, script: string) => {
    const newVideo: Video = {
      id: `vid-${Date.now()}`,
      title,
      prompt,
      script,
      status: VideoStatus.Idea,
    };
    setVideos(prev => [...prev, newVideo]);
    // Move the new idea to scripting automatically
    setTimeout(() => {
        setVideos(currentVideos => currentVideos.map(v => v.id === newVideo.id ? {...v, status: VideoStatus.Scripting} : v));
    }, 500);
  };

  const handleOpenUploadModal = (video: Video) => {
    setSelectedVideo(video);
    setUploadModalOpen(true);
  };

  const handleUpload = async (video: Video, videoFile: File) => {
    console.log(`Uploading video "${video.title}" with file:`, videoFile.name);

    // TODO: This is where you will call your Firebase Function
    // For now, we'll just simulate the process

    // 1. Move video to "Scheduled"
    setVideos(prev => prev.map(v => v.id === video.id ? { ...v, status: VideoStatus.Scheduled } : v));

    // 2. Simulate upload time and then move to "Published"
    setTimeout(() => {
       setVideos(prev => prev.map(v => v.id === video.id ? {
           ...v,
           status: VideoStatus.Published,
           youtubeUrl: `https://youtube.com/watch?v=mock-${video.id}`
        } : v));
    }, 5000); // 5-second mock upload
  };

  return (
    <div className="min-h-screen bg-brand-bg">
      <Header />
      <main>
        <ContentPipeline
          videos={videos}
          onOpenCreativeAssistant={() => setCreativeAssistantOpen(true)}
          onOpenUploadModal={handleOpenUploadModal}
        />
      </main>
      <CreativeAssistantModal
        isOpen={isCreativeAssistantOpen}
        onClose={() => setCreativeAssistantOpen(false)}
        onIdeaGenerated={handleIdeaGenerated}
      />
      <UploadModal
        video={selectedVideo}
        isOpen={isUploadModalOpen}
        onClose={() => setUploadModalOpen(false)}
        onUpload={handleUpload}
      />
    </div>
  );
}

export default App;