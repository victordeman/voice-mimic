import torch
from transformers import pipeline
import torchaudio
from pathlib import Path

def transcribe_audio(audio_path):
    """
    Transcribes audio to text using Whisper with Voice Activity Detection (VAD).
    Args:
        audio_path (str): Path to input audio file.
    Returns:
        str: Transcribed text.
    """
    # Load Whisper model
    try:
        transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device=0 if torch.cuda.is_available() else -1)
    except Exception as e:
        print(f"Error loading Whisper model: {e}")
        return ""

    # Load Silero VAD model for speech detection
    try:
        vad_model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad', model='silero_vad', force_reload=False)
        (get_speech_timestamps, _, read_audio, _, _) = utils
    except Exception as e:
        print(f"Error loading VAD model: {e}")
        return ""

    # Read audio
    audio_path = Path(audio_path)
    if not audio_path.exists():
        print(f"Audio file {audio_path} not found.")
        return ""

    audio, sample_rate = torchaudio.load(audio_path)
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        audio = resampler(audio)
        sample_rate = 16000

    # Apply VAD to detect speech
    speech_timestamps = get_speech_timestamps(audio[0], vad_model, sampling_rate=sample_rate)

    # Transcribe only if speech is detected
    if not speech_timestamps:
        print("No speech detected in audio.")
        return ""

    # Transcribe audio
    try:
        result = transcriber(audio_path, return_timestamps=True)
        text = result["text"]
        print(f"Transcribed text: {text}")
        return text.strip()
    except Exception as e:
        print(f"Transcription error: {e}")
        return ""

if __name__ == "__main__":
    # Example usage
    audio_file = "data/sample.wav"
    transcribed_text = transcribe_audio(audio_file)
    print(f"Output: {transcribed_text}")
