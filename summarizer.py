import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=api_key)

# Initialize Gemini Model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

def get_transcript(video_url):
    """Extract transcript from a YouTube video URL."""
    try:
        video_id = video_url.split("v=")[1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-IN'])
        transcript_text = " ".join([entry["text"] for entry in transcript_list])
        return transcript_text
    except Exception as e:
        return f"Error fetching transcript: {e}"

def summarize_text(text):
    """Generate a summary using Gemini AI."""
    try:
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return f"Error generating summary: {e}"

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    print("\nFetching transcript...\n")
    
    transcript = get_transcript(video_url)

    if "Error" not in transcript:
        print("\nGenerating summary...\n")
        summary = summarize_text(transcript)
        print("\n--- Video Summary ---\n")
        print(summary)
    else:
        print(transcript)
