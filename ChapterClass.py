import ChapterParser
import json

class Chapter:
    def __init__(self, text_path):
        self.original_text = ChapterParser.parseText(text_path)
        self.stats = ChapterParser.ProcessChapter(self.original_text)

    def save(self, save_name):
        with open(f"{save_name}.json", "w", encoding="UTF-8") as f:
            json.dump({"original_text": self.original_text,
                    "stats": self.stats}, f, indent=4, ensure_ascii=False)