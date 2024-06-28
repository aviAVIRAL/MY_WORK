from flask import Flask, jsonify

app = Flask(__name__)

import vertexai
import os 
from vertexai.preview.generative_models import GenerativeModel, Part

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "complete-flash-411506-1e6791534c29.json"

@app.route('/generate_story', methods=['GET'])
def generate_story():
    model = GenerativeModel("gemini-pro")
    responses = model.generate_content(
        """Generate an engaging and interactive adventure story suitable for a 4-year-old child. The protagonist, named \'Alex,\' wakes up one morning to discover a magical object in their room. This magical object has the power to transport Alex to different places and times.
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

    # Return the generated story as JSON
    return jsonify({'story': generated_text})

if __name__ == '__main__':
    app.run(debug=True, port=9000)