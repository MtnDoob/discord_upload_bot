from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok = True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Save the file to the uploads folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Return the absolute file path
    return f'The file was successfully uploaded to: {os.path.abspath(file_path)}'

if __name__ == '__main__':
    app.run(debug=True)
