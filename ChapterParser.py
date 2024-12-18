import re
from collections import Counter
import ChapterClass

def parseText(chapter_path):
    with open(chapter_path, "r", encoding="UTF-8") as f:
        text = f.read()
    return text

def splitOnParagraphs(chapter_text):
    return chapter_text.split("\n\n")

def processParagraph(paragraph):
    paragraph = paragraph.lower()
    paragraph = re.sub(r"\d+", "", paragraph)
    paragraph = re.sub(r"\W+", " ", paragraph)
    return paragraph

def countTermFrequency(paragraph):
    tokenized_paragraph = paragraph.split()
    words_count = len(tokenized_paragraph)
    counted_terms = Counter(tokenized_paragraph)
    term_frequency = {k: ChapterClass.Stat(v/words_count) for k,v in counted_terms.items()}
    return term_frequency

