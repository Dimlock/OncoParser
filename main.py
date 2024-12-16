import ChapterParser

chapter_text = ChapterParser.parseText("Главы/Вступление/Thyroid Carcinomas.txt")
chapter_list = ChapterParser.splitOnParagraphs(chapter_text)
first_paragraph = ChapterParser.processParagraph(chapter_list[0])
first_paragraph_frequency = ChapterParser.countTermFrequency(first_paragraph)
print(first_paragraph_frequency)