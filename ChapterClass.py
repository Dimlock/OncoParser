import ChapterParser
import json


class Chapter:
    def __init__(self, text_path):
        self.original_text = ChapterParser.parseText(text_path)
        self.paragraphs = self.create_paragraphs()
        self.terms = []

    def create_paragraphs(self):
        result = []
        for paragraph in ChapterParser.splitOnParagraphs(self.original_text):
            result.append(Paragraph(paragraph))
        return result


    def save(self, save_name):
        with open(f"{save_name}.json", "w", encoding="UTF-8") as f:
            json.dump({"original_text": self.original_text,
                       "paragraphs": [paragraph.save() for paragraph in self.paragraphs],
                       "terms": self.terms}, f, indent=4, ensure_ascii=False)

    def count_chapter_idfs(self):
        result = {}
        for paragraph in self.paragraphs:
            for stat in paragraph.stats:
                result[stat] = result.setdefault(stat, 0)
                result[stat] += paragraph.stats[stat].tf_idf
        self.terms = sorted(list(result.items()),key=lambda x: x[1])

class Paragraph:
    def __init__(self, paragraph_text):
        self.text = paragraph_text
        self.stats = self.processParagraph()

    def processParagraph(self):
        processed_paragraph = ChapterParser.processParagraph(self.text)
        result = ChapterParser.countTermFrequency(processed_paragraph)
        return result

    def save(self):
        return {"text": self.text,
                "stats": {k:v.save() for k,v in self.stats.items()}}

class Stat:
    def __init__(self, tf):
        self.tf = tf
        self.idf = 0
        self.tf_idf = 0

    def save(self):
        self.tf_idf = self.tf * self.idf
        return {"tf": self.tf,
                "idf": self.idf,
                "tf-idf": self.tf_idf}