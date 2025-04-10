# Use a Python base image
FROM python:3.9-slim

# Install system dependencies for building packages
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    poppler-utils \
    tesseract-ocr \
    gcc \
    g++ \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm

# Expose the API port
EXPOSE 5000

# Run the Flask app
CMD ["python", "main.py"]