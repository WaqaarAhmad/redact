from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
from redactor.processor import process_pdf

app = Flask(__name__)
UPLOAD_FOLDER = 'input'
OUTPUT_FOLDER = 'output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            output_path = os.path.join(OUTPUT_FOLDER, filename)
            file.save(input_path)
            process_pdf(input_path, output_path)
            return send_file(output_path, as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    app.run(debug=True)