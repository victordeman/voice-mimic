# Voice Mimic System

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/victordeman/voice-mimic)

## Overview

This project implements a voice mimic system that translates spoken content from one language to another while preserving the original speaker's voice characteristics. It uses a modular pipeline involving speech-to-text (STT), text translation, and text-to-speech (TTS) with voice cloning. The system is built primarily with open-source tools for local deployment.

### Key Features
- **Speech-to-Text (STT)**: Transcribes input audio using Whisper.
- **Text Refinement and Translation**: Corrects transcription and translates using an LLM like Llama 3.
- **Voice Cloning and TTS**: Clones the voice with OpenVoice and synthesizes speech in the target language.
- **User Interface**: A simple Gradio app for easy interaction.
- **Multilingual Support**: Handles various languages (e.g., English to Spanish).
- **Ethical Considerations**: Emphasizes consent for voice cloning.

## Repository Structure

- **src/**: Contains the Python source code.
  - **transcribe.py**: Handles speech-to-text transcription with Whisper and Silero VAD.
  - **translate.py**: Manages text refinement and translation using Llama 3.
  - **synthesize.py**: Performs voice cloning and TTS synthesis (placeholder for OpenVoice).
  - **app.py**: The main Gradio application interface.
- **data/**: Directory for storing voice samples and output audio files.
- **requirements.txt**: List of Python dependencies.
- **.gitignore**: Git ignore file for excluding unnecessary files.

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
   **Note**: You must manually download models:
   - Whisper: `openai/whisper-large-v3` from Hugging Face.
   - Llama 3: `meta-llama/Llama-3-8B-Instruct` from Hugging Face (requires access approval).
   - Silero VAD: Automatically downloaded via torch.hub.
   - OpenVoice: Install from MyShell's GitHub repo (`myshell-ai/OpenVoice`) and download `myshell-ai/OpenVoice-v2`.

3. **Prepare Voice Sample**:
   Place a voice sample (e.g., `original_voice_sample.wav`) in the `data/` directory. A 10-30 second clip is sufficient for testing.

4. **Run the Application**:
   ```bash
   python src/app.py
   ```
   Access the Gradio interface at `http://localhost:7860`.

## Usage

- Upload an audio file (e.g., WAV format) via the Gradio UI.
- Select the target language (e.g., 'es' for Spanish).
- The system transcribes, translates, and synthesizes audio in the cloned voice.
- Download the output audio from the interface.

### Example Workflow
1. Upload an English audio saying, "Hello, how are you?"
2. Select 'es' (Spanish) as the target language.
3. Output: Audio in Spanish ("Hola, ¿cómo estás?") with the original voice's characteristics.

## Dependencies (requirements.txt)

```
torch
numpy
scipy
transformers
torchaudio
gradio
```
**Note**: OpenVoice requires manual installation from its GitHub repository.

## Testing Notes

- **Current Limitation**: The `synthesize.py` file uses a placeholder (sine wave) for TTS due to OpenVoice's complex setup. Replace with actual OpenVoice code after installation.
- **Hardware**: A GPU is recommended for faster inference (Whisper and Llama 3). CPU works but is slower.
- **Sample Audio**: Place a sample audio file (`data/sample.wav`) for testing transcription.
- **Expected Output**: The system generates a WAV file in `data/output.wav`.

## Challenges and Improvements

- **Voice Cloning Quality**: Use longer voice samples (10+ minutes) for better cloning with OpenVoice.
- **Latency**: Optimize model loading and inference for real-time use.
- **Extensions**: Add support for more languages or integrate real-time streaming.

## License

MIT License. See LICENSE file for details.

## Contributors

- Victor Deman (victordeman)

For issues or contributions, please open a pull request on GitHub.
