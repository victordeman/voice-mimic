from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def refine_and_translate(text, target_lang="es"):
    """
    Refines transcription and translates to target language using Llama 3.
    Args:
        text (str): Input text to refine and translate.
        target_lang (str): Target language code (e.g., 'es' for Spanish).
    Returns:
        str: Translated text.
    """
    # Load Llama 3 model and tokenizer
    try:
        model_name = "meta-llama/Llama-3-8B-Instruct"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
    except Exception as e:
        print(f"Error loading Llama model: {e}")
        return ""

    # Step 1: Refine transcription
    refine_prompt = f"""
Correct and segment this transcription into complete sentences, ensuring proper grammar and punctuation:
{text}
"""
    inputs = tokenizer(refine_prompt, return_tensors="pt").to(model.device)
    try:
        refined_output = model.generate(**inputs, max_length=500, num_beams=5, no_repeat_ngram_size=2)
        refined_text = tokenizer.decode(refined_output[0], skip_special_tokens=True)
        # Extract the corrected part (remove prompt)
        refined_text = refined_text.split("Corrected transcription:")[-1].strip() if "Corrected transcription:" in refined_text else refined_text
    except Exception as e:
        print(f"Refinement error: {e}")
        return ""

    # Step 2: Translate to target language
    translate_prompt = f"""
Translate the following text to {target_lang}, preserving the original meaning and style:
{refined_text}
"""
    inputs = tokenizer(translate_prompt, return_tensors="pt").to(model.device)
    try:
        translated_output = model.generate(**inputs, max_length=500, num_beams=5, no_repeat_ngram_size=2)
        translated_text = tokenizer.decode(translated_output[0], skip_special_tokens=True)
        # Extract the translated part
        translated_text = translated_text.split("Translated text:")[-1].strip() if "Translated text:" in translated_text else translated_text
        print(f"Translated text ({target_lang}): {translated_text}")
        return translated_text
    except Exception as e:
        print(f"Translation error: {e}")
        return ""

if __name__ == "__main__":
    # Example usage
    sample_text = "Hello, how are you today? Let's talk about the weather."
    translated = refine_and_translate(sample_text, target_lang="es")
    print(f"Output: {translated}")
