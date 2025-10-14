// services/geminiService.ts

import { GoogleGenerativeAI } from "@google/genai";
import { Video } from '../types';

// IMPORTANT: Add your Gemini API key here
const API_KEY = "YOUR_GEMINI_API_KEY";

const genAI = new GoogleGenerativeAI(API_KEY);

export async function generateContent(prompt: string): Promise<Partial<Video>> {
  if (!API_KEY || API_KEY === "YOUR_GEMINI_API_KEY") {
    console.error("API Key not found. Please add your Gemini API key to geminiService.ts");
    // Return mock data if API key is not set
    return {
      title: "This is a Mock Title since API key is missing",
      script: "This is a mock script. Please add your real Gemini API key to `services/geminiService.ts` to generate content.",
    };
  }

  try {
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const fullPrompt = `
      Based on the following user prompt, generate a compelling YouTube video title and a concise script.
      The output should be in JSON format with two keys: "title" and "script".

      User Prompt: "${prompt}"

      JSON Output:
    `;

    const result = await model.generateContent(fullPrompt);
    const response = await result.response;
    const text = response.text();

    // Clean up the response to make sure it's valid JSON
    const jsonString = text.replace(/```json/g, '').replace(/```/g, '').trim();

    const parsedContent = JSON.parse(jsonString);

    return {
      title: parsedContent.title || 'Untitled',
      script: parsedContent.script || 'No script generated.',
    };
  } catch (error) {
    console.error("Error generating content with Gemini:", error);
    throw new Error("Failed to generate content.");
  }
}