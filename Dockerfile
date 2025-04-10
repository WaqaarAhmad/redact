FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y poppler-utils tesseract-ocr && \
    pip install --no-cache-dir -U pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt && python -m spacy download en_core_web_sm

CMD ["python", "gui/app.py"]