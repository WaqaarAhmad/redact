# Directory: pdf-redactor/
# Entry point: main.py

from flask import Flask, request
import os

app = Flask(__name__)

# Ensure input directory exists
INPUT_DIR = 'input'
os.makedirs(INPUT_DIR, exist_ok=True)

@app.route("/", methods=["GET"])
def health():
    return "🚀 Flask PDF Redaction API is up!"

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400

    file = request.files["file"]
    filepath = os.path.join(INPUT_DIR, file.filename)
    file.save(filepath)
    
    # TODO: Add redaction logic here

    return {"message": f"{file.filename} uploaded and ready for redaction"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

