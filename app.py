from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from werkzeug.utils import secure_filename
import os
import PyPDF2

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("API_KEY")

# Initialize Flask app and Gemini model
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint for answering questions
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    passage = data.get('passage')
    question = data.get('question')

    # Create a prompt with the passage and the question
    prompt = f"Passage: {passage}\n\nQuestion: {question}\n\nAnswer:"

    try:
        # Get the response from the Gemini model
        response = model.generate_content(prompt)
        answer = response.text.strip()
    except Exception as e:
        answer = f"Error: {str(e)}"

    return jsonify({'answer': answer})

# API endpoint to upload and extract text from PDF
@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(filepath)

        try:
            # Extract text from PDF
            with open(filepath, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                extracted_text = ' '.join(page.extract_text() for page in reader.pages)
            return jsonify({'text': extracted_text})
        except Exception as e:
            return jsonify({'error': f'Failed to extract text: {str(e)}'}), 500
    else:
        return jsonify({'error': 'Invalid file type. Only PDFs are allowed.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
