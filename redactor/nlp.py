import spacy

nlp = spacy.load("en_core_web_sm")

ENTITIES_TO_REDACT = ["PERSON", "GPE", "ORG"]

def apply_nlp_redaction(page, text):
    rects = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ENTITIES_TO_REDACT:
            matches = page.search_for(ent.text)
            rects.extend(matches)
    return rects