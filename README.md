# Voice Mimic System

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/victordeman/voice-mimic)

## Overview

This project implements a voice mimic system that translates spoken English content from MP3 audio or MP4 video to German while preserving the original speaker's voice characteristics. It uses a modular pipeline involving speech-to-text (STT), text translation, and text-to-speech (TTS) with voice cloning, built with open-source tools.

### Key Features
- **Input Support**: Accepts MP3 audio or MP4 video (audio extracted via `moviepy`).
- **Speech-to-Text (STT)**: Transcribes English audio using Whisper.
- **Text Refinement and Translation**: Refines transcription and translates to German using Llama 3.
- **Voice Cloning and TTS**: Clones the voice with OpenVoice and synthesizes German speech.
- **User Interface**: Gradio app for uploading media and voice samples.
- **Ethical Considerations**: Requires consent for voice cloning.

## Repository Structure

- **src/**: Python source code.
  - **transcribe.py**: Extracts audio from MP4 and transcribes English speech.
  - **translate.py**: Refines transcription and translates to German.
  - **synthesize.py**: Clones voice and synthesizes German speech.
  - **app.py**: Gradio app integrating the pipeline.
- **data/**: Stores voice samples (e.g., `original_voice_sample.wav`).
- **requirements.txt**: Python dependencies.
- **.gitignore**: Excludes unnecessary files from Git.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/victordeman/voice-mimic.git
   cd voice-mimic
   ```

2. **Install Dependencies**:
   Create a virtual environment and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   Download models:
   - Whisper: `openai/whisper-large-v3` from Hugging Face.
   - Llama 3: `meta-llama/Llama-3-8B-Instruct` from Hugging Face.
   - OpenVoice: `myshell-ai/OpenVoice-v2` from its repository.

3. **Prepare Voice Sample**:
   Place a WAV voice sample (e.g., `original_voice_sample.wav`) in `data/`.

4. **Run the Application**:
   ```bash
   python src/app.py
   ```
   Access the Gradio interface in your browser.

## Usage

- Upload an MP3 audio or MP4 video containing English speech.
- Upload a WAV voice sample for cloning.
- The system transcribes, translates to German, and outputs audio in the cloned voice.

## Dependencies (requirements.txt)

```
torch
numpy
scipy
transformers
gradio
moviepy
# OpenVoice requires manual installation from its repository.
```

## Testing

- **Input**: MP3 or MP4 with clear English speech.
- **Output**: WAV audio in German with the cloned voice.
- **Metrics**: Target WER <10% for transcription, BLEU >0.5 for translation, MOS ~4/5 for voice quality.

## Challenges and Improvements

- **Quality**: Longer voice samples improve cloning fidelity.
- **Latency**: Optimize models for faster inference.
- **Extensions**: Add support for more languages or real-time processing.

## License

MIT License. See LICENSE file for details.

## Contributors

- Victor Deman (victordeman)

For issues or contributions, open a pull request on GitHub.
