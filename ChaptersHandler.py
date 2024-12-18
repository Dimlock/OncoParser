import math


class ChaptersHandler:
    def __init__(self):
        self.chapters = []
        self.paragraphs = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)
        self.add_paragraphs()

    def add_paragraphs(self):
        for chapter in self.chapters:
            self.paragraphs.extend(chapter.paragraphs)

    def count_term_df(self, term):
        counter = 0
        for paragraph in self.paragraphs:
            for stat in paragraph.stats:
                if term == stat:
                    counter += 1
        return counter

    def count_idf(self, term):
        result = math.log(len(self.paragraphs) / self.count_term_df(term))
        return result

    def update_idf(self):
        for chapter in self.chapters:
            for paragraph in chapter.paragraphs:
                for stat in paragraph.stats:
                    paragraph.stats[stat].idf = self.count_idf(stat)

    def save(self):
        for i, chapter in enumerate(self.chapters):
            chapter.save(i)