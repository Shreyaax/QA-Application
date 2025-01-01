### QA-Application

```markdown


A web-based **Question-Answering System** that allows users to upload a PDF, extract text from it, and ask questions based on the extracted content. The application uses **Flask** for the backend, **Google Generative AI** for question answering, and a responsive web interface for user interactions.

---

## Features

- **Upload PDFs**: Extract text from uploaded PDF files.
- **Question Answering**: Ask questions based on the extracted text or manually entered passages.
- **Responsive Interface**: User-friendly web interface built with HTML, CSS, and JavaScript.
- **Google Generative AI Integration**: Leverages Google's Gemini model for generating answers.

## Directory Structure

```
Shreyaax-QA-Application/
├── app.py                     # Flask application logic
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html             # HTML file for the web interface
├── static/
│   ├── css/
│   │   └── style.css          # CSS styles
│   └── js/
│       └── script.js          # JavaScript logic
└── uploads/                   # Directory to store uploaded PDFs
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)
- A valid **Google Generative AI API Key**

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Shreyaax-QA-Application.git
   cd Shreyaax-QA-Application
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root:
     ```
     API_KEY=your_google_genai_api_key
     ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   - Open your browser and navigate to: `http://127.0.0.1:5000`

---

## Usage

1. **Upload PDF**: Use the "Upload a PDF" section to upload a file and extract its text.
2. **Enter a Passage**: Manually paste a passage or use the extracted text.
3. **Ask Questions**: Type your question and submit to receive an answer.
4. **View Answer**: The generated answer will be displayed in the "The Answer" section.

---

## Technologies Used

### Backend
- **Flask**: Lightweight web framework
- **Python-Dotenv**: For managing environment variables
- **Google Generative AI**: Gemini model for content generation
- **PyPDF2**: Extracting text from PDF files

### Frontend
- **HTML**: Web structure
- **CSS**: Styling with a soft green gradient theme
- **JavaScript**: Form handling and AJAX requests

---

## Future Enhancements
- **Authentication**: Add user authentication for API key security.
- **Multi-File Support**: Allow multiple PDF uploads and text merging.
- **Answer Refinement**: Improve the model's response through fine-tuning prompts.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature"`.
4. Push to your fork: `git push origin feature-name`.
5. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **Google Generative AI** for enabling state-of-the-art content generation.
- **Flask Community** for excellent documentation and support.

---


Let me know if you'd like to customize this further!
