from django.shortcuts import render
from transformers import MarianMTModel, MarianTokenizer

def home(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')

        # Load the pre-trained model and tokenizer
        model_name = 'Helsinki-NLP/opus-mt-ig-en'
        model = MarianMTModel.from_pretrained(model_name)
        tokenizer = MarianTokenizer.from_pretrained(model_name)

        # Tokenize the input text
        input_ids = tokenizer.encode(input_text, return_tensors='pt')

        # Generate translation
        translation_ids = model.generate(input_ids)

        # Decode the translated text
        translated_text = tokenizer.decode(translation_ids[0], skip_special_tokens=True)

        return render(request, 'base/home.html', {'input_text': input_text, 'translated_text': translated_text})

    return render(request, 'base/home.html')
