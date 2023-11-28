from django.shortcuts import render
import pyaudio
from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1.types import RecognitionConfig
from .translate import translate_to_igbo

def home(request):
    if request.method == 'POST':
        # Initialize PyAudio
        p = pyaudio.PyAudio()

        # Set the audio format and other parameters based on your requirements
        format = pyaudio.paInt16
        channels = 1
        rate = 16000
        chunk = 1024

        stream = p.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

        print("Listening...")

        frames = []
        for i in range(0, int(rate / chunk * 5)):  # Adjust the time based on your needs
            data = stream.read(chunk)
            frames.append(data)

        print("Stopped listening.")

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Convert the audio frames to bytes
        audio_content = b''.join(frames)

        # Perform Speech-to-Text
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(content=audio_content)
        config = speech.RecognitionConfig(
            encoding=RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=rate,
            language_code="en-US",
        )

        # Perform the Speech-to-Text API call
        response = client.recognize(config=config, audio=audio)

        # Extract English text from the response
        english_text = response.results[0].alternatives[0].transcript
        print(response.results)
        print(response.results[0].alternatives)
        print(response.results[0].alternatives[0].transcript)

        # Perform English to Igbo translation
        igbo_text = translate_to_igbo(english_text)

        return render(request, 'base/home.html', {'english_text': english_text, 'igbo_text': igbo_text})

    return render(request, 'base/home.html')
