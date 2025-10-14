// types.ts

export enum VideoStatus {
  Idea = 'Idea',
  Scripting = 'Scripting',
  Scheduled = 'Scheduled',
  Published = 'Published',
}

export interface Video {
  id: string;
  title: string;
  prompt: string;
  script: string;
  status: VideoStatus;
  youtubeUrl?: string;
}