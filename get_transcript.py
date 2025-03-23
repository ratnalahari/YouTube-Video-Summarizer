from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        # Try to get the manually created English transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    except:
        try:
            # If the manually created one is not available, get the auto-generated English transcript
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-IN'])
        except Exception as e:
            return f"Error: {str(e)}"

    text = " ".join([t['text'] for t in transcript])
    return text

if __name__ == "__main__":
    video_id = "RdqrcZnzELU"  # Your video ID
    print(get_transcript(video_id))
