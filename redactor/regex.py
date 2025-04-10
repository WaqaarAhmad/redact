import re

def apply_regex_redaction(page, text):
    patterns = [
        r"\b\d{3}-\d{2}-\d{4}\b",  # SSN
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",  # Email
    ]
    rects = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            found = page.search_for(match)
            rects.extend(found)
    return rects