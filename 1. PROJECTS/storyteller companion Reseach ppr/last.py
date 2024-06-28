import os
import pyaudio
import speech_recognition as sr
import google.cloud.texttospeech as tts
import tempfile
import pygame
import webbrowser
import vertexai
from vertexai.preview.generative_models import GenerativeModel

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "complete-flash-411506-1e6791534c29.json"

def recognize_speech():
    client = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        # Adjust the recognizer sensitivity to ambient noise
        client.adjust_for_ambient_noise(source)
        audio = client.listen(source)
    try:
        phrase = client.recognize_google(audio, language="en-US")
        print("You said:", phrase)

        # Check if the phrase contains specific keywords
        if "hello" in phrase.lower():
            return "hello"
        elif "namaste" in phrase.lower():
            return "nam"
        elif "open the chrome" in phrase.lower():
            return "open_chrome"
        elif any(keyword in phrase.lower() for keyword in [ "write the story", "generate the story", "tell me a story","narrate me a story", "can you write the story", "can you narrate me a story","write story"]):
            return "generate_story"   
        # elif any(keyword in phrase.lower() for keyword in []):
        #     return "write_story"
        else:
            print("Command not recognized.")
            return None

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def text_to_wav(text: str, voice_name: str = 'en-AU-Neural2-A'):
    # Check if the provided text is empty
    if not text:
        print("Provided text is empty. Exiting.")
        return

    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()

    try:
        response = client.synthesize_speech(
            input=text_input,
            voice=voice_params,
            audio_config=audio_config,
        )

        # Create a temporary file to save the synthesized speech
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as out:
            out.write(response.audio_content)
            print(f'Generated speech saved to "{out.name}"')
            return out.name
    except Exception as e:
        print(f"Error during text-to-speech synthesis: {e}")

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def generate_story():
    model = GenerativeModel("gemini-pro")
    responses = model.generate_content(
        """Generate an engaging and interactive adventure story suitable for a 4-year-old child. The protagonist, named \'Avi-ral,\' wakes up one morning to discover a magical object in their room. This magical object has the power to transport Alex to different places and times.
        The story should revolve around themes of adventure, honesty, and hard work. Incorporate moments where Alex faces challenges that require honesty and hard work to overcome. Make the narrative interactive, allowing for child input to influence the plot. If the child provides an input during the story, ensure that the plot adapts accordingly.
        Introduce vivid descriptions, simple language, and positive messages. Additionally, include questions at key points in the story to keep the child engaged, such as \'What should Alex do next?\' or \'How can Alex solve this problem?\'
        Please ensure that the generated story is age-appropriate, imaginative, and conveys positive moral values. The goal is to create an entertaining and educational adventure for a young audience.""",
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.9,
            "top_p": 1
        },
        stream=True,
    )
  
    generated_text = ''.join(response.text if hasattr(response, 'text') else '' for response in responses)
    print("Generated story:")
    print(generated_text)

    # Synthesize the generated story into speech
    response_wav_file = text_to_wav(generated_text)

    # Play the synthesized story
    play_audio(response_wav_file)

if __name__ == "__main__":
    while True:
        # Keep listening continuously
        input_text = recognize_speech()
        if input_text:
            if input_text == "hello":
                # Synthesize response
                response_text = "Hello Avi-ral, how can i help you?"
                response_wav_file = text_to_wav(response_text)

                # Play the synthesized response
                play_audio(response_wav_file) 
            elif input_text == "open_chrome":
                # Open Chrome
                webbrowser.open('https://www.google.com')
                # Synthesize response
                response_text = "Chrome is opening."
                response_wav_file = text_to_wav(response_text)

                # Play the synthesized response
                play_audio(response_wav_file)
            elif input_text == "nam":
                response_text = "namaste Avi-ral"
                response_wav_file = text_to_wav(response_text)
                play_audio(response_wav_file)
            # elif input_text == "write_story":
            #     # Synthesize response
            #     response_text = "Sure! What type of story would you like to listen to?"
            #     response_wav_file = text_to_wav(response_text)

            #     # Play the synthesized response
            #     play_audio(response_wav_file) 
            elif input_text == "generate_story":
                # Generate story
                generate_story()
        else:
            continue