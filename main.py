import ChapterClass
import pathlib

for i, file in enumerate(pathlib.Path("Главы/").rglob("*.txt")):
    print(ChapterClass.Chapter(file).save(i))