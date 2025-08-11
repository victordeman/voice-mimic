import gradio as gr
from transcribe import transcribe_audio
from translate import refine_and_translate
from synthesize import synthesize_with_clone

def process_media(media_path, voice_sample_path="data/original_voice_sample.wav"):
    """Process MP3/MP4 input, translate to German, and synthesize in cloned voice."""
    try:
        # Step 1: Transcribe English audio
        transcribed_text = transcribe_audio(media_path)
        if not transcribed_text:
            return None, "Transcription failed."
        
        # Step 2: Translate to German
        translated_text = refine_and_translate(transcribed_text, target_lang="de")
        if not translated_text:
            return None, "Translation failed."
        
        # Step 3: Synthesize with cloned voice
        output_audio = synthesize_with_clone(voice_sample_path, translated_text)
        if not output_audio:
            return None, "Synthesis failed."
        
        return output_audio, f"Transcription: {transcribed_text}\nTranslated (German): {translated_text}"
    except Exception as e:
        return None, f"Error: {str(e)}"

# Gradio interface
iface = gr.Interface(
    fn=process_media,
    inputs=[
        gr.File(label="Upload MP3 or MP4", file_types=[".mp3", ".mp4"]),
        gr.File(label="Voice Sample (WAV)", file_types=[".wav"])
    ],
    outputs=[
        gr.Audio(label="Output Audio (German)"),
        gr.Textbox(label="Transcription and Translation")
    ],
    title="Voice Mimic: English to German",
    description="Upload an MP3 audio or MP4 video and a WAV voice sample to translate English speech to German in the same voice."
)
iface.launch()
