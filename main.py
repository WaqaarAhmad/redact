# Directory: pdf-redactor/
# Entry point: main.py

import os
from redactor.processor import process_pdf

INPUT_DIR = '/app/input'
OUTPUT_DIR = '/app/output'

if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR)

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".pdf"):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)
        process_pdf(input_path, output_path)
        print(f"Redacted: {filename}")


