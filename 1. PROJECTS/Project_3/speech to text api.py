speech_to_text_api.py
import pygame
from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
import os

# Set Google Cloud credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-google-cloud-credentials.json"

# Initialize Pygame
pygame.init()

# Initialize Pygame's microphone
pygame.mixer.init()

# Create a Speech-to-Text client
client = speech_v1p1beta1.SpeechClient()

# Define a function to transcribe speech from the microphone
def transcribe_microphone():
    config = {
        "encoding": enums.RecognitionConfig.AudioEncoding.LINEAR16,
        "sample_rate_hertz": 16000,
        "language_code": "en-US",
    }

    # Open the microphone
    pygame.mixer.pre_init(44100, -16, 1, 1024)
    pygame.mixer.init()
    pygame.mixer.music.load("blank.mp3")
    pygame.mixer.music.play(-1)

    # Record audio from the microphone
    recording = pygame.mixer.Sound("recording.wav")
    recording.play()
    pygame.time.wait(3000)  # Adjust the recording time as needed

    # Stop recording
    recording.stop()

    with open("recording.wav", "rb") as f:
        audio_content = f.read()

    audio = {"content": audio_content}

    # Perform speech recognition
    response = client.recognize(config=config, audio=audio)

    # Process the response
    for result in response.results:
        print("Transcription: {}".format(result.alternatives[0].transcript))

    # Clean up
    pygame.mixer.quit()

# Call the function to start transcribing from the microphone
transcribe_microphone()