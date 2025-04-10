import fitz  # PyMuPDF
from .regex import apply_regex_redaction
from .ocr import extract_text_with_ocr
from .nlp import apply_nlp_redaction

def process_pdf(input_path, output_path):
    doc = fitz.open(input_path)
    for page in doc:
        text = page.get_text()
        if not text.strip():
            text = extract_text_with_ocr(page)
        areas_regex = apply_regex_redaction(page, text)
        areas_nlp = apply_nlp_redaction(page, text)
        for area in areas_regex + areas_nlp:
            page.add_redact_annot(area, fill=(0, 0, 0))
        page.apply_redactions()
    doc.save(output_path)
