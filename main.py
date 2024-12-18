import ChapterClass
import pathlib
import ChaptersHandler

ChapterHandler = ChaptersHandler.ChaptersHandler()
#for i, file in enumerate(pathlib.Path("Главы/").rglob("*.txt")):
#    print(ChapterClass.Chapter(file).save(i))

for file in pathlib.Path("Главы/").rglob("*.txt"):
    ChapterHandler.add_chapter(ChapterClass.Chapter(file))
ChapterHandler.update_idf()
ChapterHandler.save()