from openvoice import OpenVoiceModel
import scipy.io.wavfile
import os

def synthesize_with_clone(voice_sample_path, text, output_path="output.wav", target_lang="de"):
    """Synthesize German text in the cloned voice."""
    # Load OpenVoice model (assumes OpenVoice-v2 is downloaded)
    model = OpenVoiceModel.from_pretrained("myshell-ai/OpenVoice-v2")
    
    try:
        # Extract tone color from voice sample
        tone_color = model.extract_tone_color(voice_sample_path)
        
        # Generate speech
        audio = model.generate(text=text, tone_color=tone_color, language=target_lang)
        
        # Save audio to WAV
        scipy.io.wavfile.write(output_path, rate=22050, data=audio)
        return output_path
    except Exception as e:
        print(f"Synthesis error: {e}")
        return None
