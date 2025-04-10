from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import tempfile

def extract_text_with_ocr(page):
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(tmp.name, format="PNG")
        text = pytesseract.image_to_string(Image.open(tmp.name))
    return text