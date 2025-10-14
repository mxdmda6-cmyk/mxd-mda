// src/firebase.ts

import { initializeApp } from 'firebase/app';
import { getAuth, signInAnonymously, onAuthStateChanged } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import { getStorage } from 'firebase/storage';
import { getFunctions } from 'firebase/functions';

// --- IMPORTANT ---
// PASTE YOUR FIREBASE CONFIG OBJECT HERE
const firebaseConfig = {
  apiKey: "AIza....",
  authDomain: "your-project-id.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project-id.appspot.com",
  messagingSenderId: "...",
  appId: "..."
};
// -----------------

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Export the services you need
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);
export const functions = getFunctions(app);

// Simple utility to get the current user's auth state
export function onAuth(callback: (user: any) => void) {
  return onAuthStateChanged(auth, callback);
}

// Simple sign-in function
export function login() {
  return signInAnonymously(auth);
}