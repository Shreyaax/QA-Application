document.getElementById('pdf-form').addEventListener('click', async function (event) {
    if (event.target.id === 'extract-btn') {
        const fileInput = document.getElementById('pdf-file');
        const file = fileInput.files[0];

        if (!file) {
            alert('Please upload a PDF file.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Failed to extract text from the PDF.');
            }

            const data = await response.json();
            if (data.error) {
                throw new Error(data.error);
            }

            document.getElementById('passage').value = data.text;
        } catch (error) {
            alert(error.message);
        }
    }
});

document.getElementById('qa-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const passage = document.getElementById('passage').value;
    const question = document.getElementById('question').value;

    const button = event.target.querySelector('button');
    const originalText = button.textContent;

    // Show loading animation on button
    button.textContent = "Fetching...";
    button.disabled = true;

    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ passage, question }),
        });

        if (!response.ok) {
            throw new Error('Error fetching the answer. Please try again.');
        }

        const data = await response.json();
        document.getElementById('answer').textContent = data.answer || 'No answer found.';
    } catch (error) {
        document.getElementById('answer').textContent = error.message;
    } finally {
        // Restore button state
        button.textContent = originalText;
        button.disabled = false;
    }
});
