import gradio as gr
from transcribe import transcribe_audio
from translate import refine_and_translate
from synthesize import synthesize_with_clone
from pathlib import Path

def process_audio(audio_path, target_lang):
    """
    Processes input audio through transcription, translation, and synthesis.
    Args:
        audio_path (str): Path to input audio.
        target_lang (str): Target language code.
    Returns:
        str: Path to output audio.
    """
    # Step 1: Transcribe
    print("Starting transcription...")
    text = transcribe_audio(audio_path)
    if not text:
        return "Error during transcription."

    # Step 2: Translate
    print("Starting translation...")
    translated_text = refine_and_translate(text, target_lang)
    if not translated_text:
        return "Error during translation."

    # Step 3: Synthesize
    print("Starting synthesis...")
    voice_sample = "data/original_voice_sample.wav"
    output_audio = synthesize_with_clone(voice_sample, translated_text, target_lang)
    if not output_audio:
        return "Error during synthesis."

    return output_audio

# Gradio interface
iface = gr.Interface(
    fn=process_audio,
    inputs=[
        gr.Audio(source="upload", type="filepath", label="Upload Audio"),
        gr.Dropdown(choices=["es", "fr", "de"], label="Target Language", value="es")
    ],
    outputs=gr.Audio(label="Output Audio"),
    title="Voice Mimic System",
    description="Upload an audio file and select a target language to translate and mimic the voice."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
