
---

# ✨ Gemini AI Translator

A simple yet elegant web application built with Flask that leverages the power of Google's Gemini 1.5 Flash model to provide fast and accurate text translations between 20+ languages.

---

## 🚀 Features

-   **Multi-Language Support**: Translate text between a wide variety of languages including English, Arabic, Spanish, Japanese, and more.
-   **Modern UI**: A clean, responsive, and user-friendly interface for a seamless experience.
-   **Powered by Gemini AI**: Utilizes Google's state-of-the-art `gemini-1.5-flash` model for high-quality, context-aware translations.
-   **Secure**: Uses environment variables to keep your API key safe and out of the source code.
-   **Lightweight**: Built with the minimalistic and powerful Flask web framework.

## 🛠️ Tech Stack

-   **Backend**: Python, Flask
-   **AI Model**: Google Gemini (`google-generativeai`)
-   **Frontend**: HTML5, CSS3
-   **Environment Management**: `python-dotenv`

## ⚙️ Setup and Installation

Follow these steps to get the application running on your local machine.

### Prerequisites

-   Python 3.8+
-   `pip` (Python package installer)
-   A Google AI API Key. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 1. Clone the Repository

Clone this project to your local machine.

```bash
git clone https://github.com/azario0/gemini-translator.git
cd gemini-translator
```
*(Replace `gemini-translator` with your actual repository name if it's different.)*

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

The application requires your Google AI API key to function.

1.  Create a new file named `.env` in the root of the project directory.
2.  Add your API key to this file as shown below:

    ```ini
    # .env
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

    Replace `"YOUR_API_KEY_HERE"` with your actual API key.

    **IMPORTANT**: The `.env` file is included in `.gitignore` by default to prevent you from accidentally committing your secret key to version control.

## ▶️ Running the Application

Once the setup is complete, you can run the Flask development server with a single command:

```bash
flask run
```

The application will be available in your web browser at:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

## 📂 Project Structure

Here is an overview of the project's file structure:

```
/gemini-translator
|
|-- /static
|   |-- /css
|       |-- style.css         # All application styles
|
|-- /templates
|   |-- index.html            # Main HTML template for the UI
|
|-- .env                      # Stores secret keys (ignored by git)
|-- .gitignore                # Specifies files for git to ignore
|-- app.py                    # Main Flask application logic
|-- requirements.txt          # List of Python dependencies
|-- README.md                 # You are here!
```

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
