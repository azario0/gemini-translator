import os
import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Initializations ---
app = Flask(__name__)

# --- Language Data ---
# Pulled from your notebook
LANGUAGES = [
    "english", "french", "arabic", "spanish", "german", "italian",
    "portuguese", "russian", "chinese (simplified)", "chinese (traditional)",
    "japanese", "korean", "turkish", "hindi", "bengali", "urdu",
    "swahili", "dutch", "greek", "polish"
]

# --- Gemini AI Configuration ---
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    # Handle initialization error gracefully
    print(f"Error initializing Gemini model: {e}")
    model = None

# --- Prompt Template ---
# This function creates the detailed prompt for the AI
def create_translation_prompt(source_lang, target_lang, user_text):
    return f"""
    You are a professional translator.

    Task:
    - Translate strictly from **{source_lang}** to **{target_lang}**.
    - Do not explain, comment, or add anything else.
    - If the text is already in {target_lang}, return it unchanged.
    - Ensure the translation is natural and context-appropriate.

    Text to translate:
    \"\"\"{user_text}\"\"\"

    Return only the translated text.
    """

# --- Flask Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    translation_result = ""
    original_text = ""
    source_lang_selected = "english"
    target_lang_selected = "arabic"
    error_message = ""

    if model is None:
        error_message = "The translation service is currently unavailable due to a configuration error."
        return render_template('index.html', languages=LANGUAGES, error=error_message)

    if request.method == 'POST':
        source_lang_selected = request.form.get('source_language')
        target_lang_selected = request.form.get('target_language')
        original_text = request.form.get('user_text')

        if not original_text:
            error_message = "Please enter some text to translate."
        elif source_lang_selected == target_lang_selected:
            error_message = "Source and target languages cannot be the same."
        else:
            try:
                # Create the prompt and generate content
                prompt = create_translation_prompt(
                    source_lang_selected,
                    target_lang_selected,
                    original_text
                )
                response = model.generate_content(prompt)
                translation_result = response.text.strip()
            except Exception as e:
                print(f"An error occurred during translation: {e}")
                error_message = f"An error occurred: {e}"

    return render_template(
        'index.html',
        languages=LANGUAGES,
        translation=translation_result,
        original_text=original_text,
        source_language_selected=source_lang_selected,
        target_language_selected=target_lang_selected,
        error=error_message
    )

if __name__ == '__main__':
    app.run(debug=True)