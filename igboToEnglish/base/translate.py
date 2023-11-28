from transformers import MarianMTModel, MarianTokenizer

def translate_to_igbo(english_text):
    model_name = "Helsinki-NLP/opus-mt-en-igbo"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize and translate the text
    inputs = tokenizer(english_text, return_tensors="pt", truncation=True)
    translation = model.generate(**inputs)
    igbo_text = tokenizer.batch_decode(translation, skip_special_tokens=True)

    return igbo_text[0] if igbo_text else "Translation not available"
