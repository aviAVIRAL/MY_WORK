api.py
from flask import Flask, request, jsonify
from vertexai.preview.generative_models import GenerativeModel
import google.cloud.texttospeech as tts
from google.cloud import speech
import base64
import os

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "complete-flash-411506-1e6791534c29.json"

def generate_story(adventure, age, honesty, hard_work):
    model = GenerativeModel("gemini-pro")
    story_template = f"""Generate an {adventure} and interactive adventure story suitable for a {age} child. The protagonist, named 'david,' wakes up one morning to discover a magical object in their room. This magical object has the power to transport david to different places and times.
The story should revolve around themes of {adventure}, {honesty}, and {hard_work}. Incorporate moments where david faces challenges that require {honesty} and {hard_work} to overcome. Make the narrative interactive, allowing for child input to influence the plot. If the child provides an input during the story, ensure that the plot adapts accordingly.
Introduce vivid descriptions, simple language, and positive messages. Additionally, include questions at key points in the story to keep the child engaged, such as 'What should david do next?' or 'How can david solve this problem?'
Please ensure that the generated story is age-appropriate, imaginative, and conveys positive moral values. The goal is to create an entertaining and educational adventure for a young audience."""
    
    responses = model.generate_content(
        story_template,
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.9,
            "top_p": 1
        },
        stream=True,
    )
    
    generated_text = ''.join(response.text if hasattr(response, 'text') else '' for response in responses)
    return generated_text

def text_to_wav(voice_name: str, text: str):
    # Check if the generated text is empty
    if not text:
        print("Generated text is empty. Exiting.")
        return

    # Debugging statement: print the generated text
    print("Generated text:")
    # print(text)

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

        filename = f"{voice_name}.wav"
        with open(filename, "wb") as out:
            out.write(response.audio_content)
            print(f'Generated speech saved to "{filename}"')
    except Exception as e:
        print(f"Error during text-to-speech synthesis: {e}")

# store generate and text to speech url(http://127.0.0.1:8012/generate_custom_story)

@app.route('/generate_custom_story', methods=['POST'])
def generate_custom_story():
    user_input = request.get_json()

    # Extract user input for placeholders
    adventure = user_input.get('adventure', 'engaging')
    age = user_input.get('age', '4-year-old')
    honesty = user_input.get('honesty', 'honesty')
    hard_work = user_input.get('hard_work', 'hard work')

    # Generate the custom story
    generated_text = generate_story(adventure, age, honesty, hard_work)

    # Call the text_to_wav function to convert the generated text to speech
    voice_name = 'en-AU-Neural2-A'  # Replace with the actual voice name you want to use
    text_to_wav(voice_name, generated_text)
    
    return jsonify({'generated_text': generated_text, 'speech_generated': True})




os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "complete-Xn1-78-flash-1893332e"
client = speech.SpeechClient()

def convert_wav_to_base64(file_path):
    with open(file_path, 'rb') as file:
        wav_data = file.read()
        base64_data = base64.b64encode(wav_data).decode('utf-8')
    return base64_data

# speech to text url(http://127.0.0.1:8012/transcribe)

@app.route('/transcribe', methods=['POST'])     
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file:
        # Save the uploaded file
        file_path = "uploaded_file.wav"
        file.save(file_path)

        # Convert the file to base64
        base64_data = convert_wav_to_base64(file_path)

        # Transcribe speech
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code="en-US",
            model="default",
            audio_channel_count=1,
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        )

        # Detects speech in the audio file
        audio = speech.RecognitionAudio(content=base64_data)
        operation = client.long_running_recognize(config=config, audio=audio)

        try:
            response = operation.result(timeout=90)
            transcripts = [result.alternatives[0].transcript for result in response.results]
            return jsonify({"transcripts": transcripts})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            # Optionally, you can remove the uploaded file after transcription
            os.remove(file_path)




if __name__ == "__main__":
    app.run(debug=True, port=8000)
