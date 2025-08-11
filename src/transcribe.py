import torch
from transformers import pipeline
import moviepy.editor as mp
import os

def extract_audio_from_video(video_path, audio_output="temp_audio.wav"):
    """Extract audio from MP4 video."""
    try:
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(audio_output)
        video.close()
        return audio_output
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None

def transcribe_audio(input_path):
    """Transcribe English audio (MP3 or MP4) to text."""
    # Check if input is MP4, extract audio if so
    if input_path.endswith(".mp4"):
        audio_path = extract_audio_from_video(input_path)
        if not audio_path:
            raise ValueError("Failed to extract audio from video.")
    else:
        audio_path = input_path
    
    # Load Whisper model (assumes whisper-large-v3 is downloaded)
    transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")
    
    # Transcribe audio
    try:
        result = transcriber(audio_path, return_timestamps=False, language="en")
        text = result["text"]
        
        # Clean up temp audio file if created
        if input_path.endswith(".mp4") and os.path.exists(audio_path):
            os.remove(audio_path)
        
        return text
    except Exception as e:
        print(f"Transcription error: {e}")
        return ""
