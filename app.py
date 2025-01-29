from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.cloud import translate_v2 as translate
import langid

# Load environment variables from .env file
load_dotenv()

# Debug: Print environment variables
print("GOOGLE_APPLICATION_CREDENTIALS:", os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
print("GEMINI_API_KEY:", os.getenv('GEMINI_API_KEY'))
print("SECRET_KEY:", os.getenv('SECRET_KEY'))

# Access environment variables
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Check if required environment variables are set
if not GEMINI_API_KEY or not SECRET_KEY or not GOOGLE_APPLICATION_CREDENTIALS:
    raise ValueError("Missing required environment variables. Check your .env file.")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize translation client
translate_client = translate.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('message', '').strip().lower()
    target_language = request.form.get('language', 'en')  # Default to English

    # Translate the input to English for processing
    if target_language != 'en':
        try:
            translated_input = translate_client.translate(user_input, target_language="en")['translatedText']
        except Exception as e:
            translated_input = user_input
    else:
        translated_input = user_input

    # Process the translated input with Gemini
    try:
        model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")
        chat_session = model.start_chat()

        prompt = f"""
        As a Healey Library expert, provide a helpful response to this question about library. Your response must:
        1. Start with "Hi!" or a similar greeting on the first line
        2. Follow with a brief introduction sentence
        3. Use ONLY dash/hyphen (-) for bullet points (not *, • or **)
        4. Put each bullet point on a new line
        5. Replace any ** with bullet points using -

        Question: {translated_input}
        """

        response = chat_session.send_message(prompt)
        answer = response.text.strip()

        # Translate the response back to the user's selected language
        if target_language != 'en':
            try:
                answer = translate_client.translate(answer, target_language=target_language)['translatedText']
            except Exception as e:
                pass  # Keep the answer in English if translation fails

        return jsonify({'answer': answer})

    except Exception as e:
        error_response = """Hi! I apologize, but I'm having trouble right now.

- Please try asking your question again
- Make sure your question is about Canvas LMS
- Try rephrasing your question
- Break down complex questions into simpler ones"""

        # Translate the error response to the user's selected language
        if target_language != 'en':
            try:
                error_response = translate_client.translate(error_response, target_language=target_language)['translatedText']
            except Exception as e:
                pass  # Keep the error response in English if translation fails

        return jsonify({'answer': error_response})

if __name__ == '__main__':
    app.run(debug=True)