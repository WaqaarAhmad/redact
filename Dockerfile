# Use a Python base image
FROM python:3.9-slim

# Set up dependencies
RUN apt-get update && \
    apt-get install -y poppler-utils tesseract-ocr && \
    pip install --no-cache-dir -U pip

# Copy the application code
COPY . /app
WORKDIR /app

# Install the Python dependencies
RUN pip install -r requirements.txt && python -m spacy download en_core_web_sm

# Expose the API port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]