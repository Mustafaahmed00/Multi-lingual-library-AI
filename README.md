## Healey Library Assistant
## Project in Progress
## Some features are under development and will be implemented soon.

The Healey Library Assistant is a web-based application designed to assist users with language translation. It allows users to input text in any language, translates it to their desired language, and provides both text and voice output for the translated text. This tool is particularly useful for multilingual communication and learning.

Features
Language Translation: Translates user input into the desired language using Google Translate API.

Voice Input: Users can speak their input instead of typing (powered by the Web Speech API).

Voice Output: The translated text is spoken aloud in the selected language.

Language Selection: Users can choose their preferred language from a dropdown menu.

Simple Interface: Easy-to-use chat-like interface for seamless interaction.

Technologies Used
Frontend: HTML, CSS, JavaScript (Web Speech API for voice input/output)

Backend: Python (Flask framework)

Translation API: Google Cloud Translation API

Speech Synthesis: Web Speech API (built into modern browsers)

Setup Instructions
Prerequisites
Python 3.x: Ensure Python is installed on your system.

Google Cloud Account: You need a Google Cloud account with the Translation API enabled.

API Keys:

Obtain a Google Cloud Translation API key.

Save the API key and service account credentials in a .env file.

Steps to Run the Application
Clone the Repository:


git clone https://github.com/your-repo/healey-library-assistant.git
cd healey-library-assistant
Set Up Environment Variables:
Create a .env file in the root directory and add the following:


GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"
SECRET_KEY="your-secret-key"
Install Dependencies:
Install the required Python packages:


pip install flask google-cloud-translate python-dotenv
Run the Application:
Start the Flask development server:


python app.py
Access the Application:
Open your browser and navigate to the url. 

How to Use
Select Language:

Choose your desired language from the dropdown menu.

Input Text:

Type your text in the input box or click the microphone button to use voice input.

Translate:

Click the "Send" button to translate the text.

Listen to Translation:

The translated text will appear in the chat box and will be spoken aloud in the selected language.

Example Usage
Select Language: Choose "Hindi" from the dropdown.

Input Text: Type "Hello, how are you?" or use voice input.

Translate: Click "Send".

Output:

Translated Text: "नमस्ते, आप कैसे हैं?"

The translated text will be spoken aloud in Hindi.

Troubleshooting
Voice Input Not Working:

Ensure your browser supports the Web Speech API (e.g., Chrome, Edge).

Allow microphone access when prompted.

Translation Errors:

Check your Google Cloud Translation API credentials in the .env file.

Ensure the Translation API is enabled in your Google Cloud Console.

Speech Synthesis Not Working:

Ensure your browser supports speech synthesis.

Check the console for any errors.

Future Enhancements
Question-Answer Feature: Add support for answering library-related questions.

Multi-language Support: Expand the list of supported languages.
