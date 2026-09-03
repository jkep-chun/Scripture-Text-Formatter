import re

def format_scripture(text: str) -> str:
    """
    Formats scripture references for easy import into Anki.

    Args:
        text (str): The input text containing scripture references in the following format: "{verse number} {text of the verse with carriage return at the end of paragraphs}".
    """
    paragraphs = [p.strip() for p in text.strip().splitlines() if p.strip()]
    formatted_paragraphs = []

    for p in paragraphs:
        p = re.sub(r"(\d+)\s+", r"<sup>\1</sup> ", p)  # Format verse numbers as superscript
        p = re.sub(r"\s+(\d+)\s+", r"\n<sup>\1</sup> ", p)  # Add line breaks before verse numbers
        formatted_paragraphs.append(p + " <br><br>")  # Add line breaks at the end of paragraphs

    return "\n".join(formatted_paragraphs)
