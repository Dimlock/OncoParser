import re
from collections import Counter

def parseText(chapter_path):
    with open(chapter_path, "r", encoding="UTF-8") as f:
        text = f.read()
    return text

def _splitOnParagraphs(chapter_text):
    return chapter_text.split("\n\n")

def _processParagraph(paragraph):
    paragraph = paragraph.lower()
    paragraph = re.sub(r"\d+", "", paragraph)
    paragraph = re.sub(r"\W+", " ", paragraph)
    return paragraph

def _countTermFrequency(paragraph):
    tokenized_paragraph = paragraph.split()
    words_count = len(tokenized_paragraph)
    counted_terms = Counter(tokenized_paragraph)
    term_frequency = {k: v/words_count for k,v in counted_terms.items()}
    return Counter(term_frequency).most_common()

def ProcessChapter(parsed_text):
    paragraphs_list = _splitOnParagraphs(parsed_text)
    processed_paragraphs = [_processParagraph(paragraph) for paragraph in paragraphs_list]
    TF_paragraphs = [_countTermFrequency(paragraph) for paragraph in processed_paragraphs]
    return TF_paragraphs