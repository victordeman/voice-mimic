from transformers import AutoModelForCausalLM, AutoTokenizer

def refine_and_translate(text, target_lang="de"):
    """Refine English transcription and translate to German."""
    # Load Llama 3 model (assumes Llama-3-8B-Instruct is downloaded)
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3-8B-Instruct")
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3-8B-Instruct")
    
    # Refine transcription
    refine_prompt = f"Correct this English transcription for grammar and clarity: {text}"
    inputs = tokenizer(refine_prompt, return_tensors="pt")
    refined_output = model.generate(**inputs, max_length=500)
    refined_text = tokenizer.decode(refined_output[0], skip_special_tokens=True)
    
    # Translate to German
    translate_prompt = f"Translate this English text to German while preserving meaning: {refined_text}"
    inputs = tokenizer(translate_prompt, return_tensors="pt")
    translated_output = model.generate(**inputs, max_length=500)
    translated_text = tokenizer.decode(translated_output[0], skip_special_tokens=True)
    
    return translated_text
