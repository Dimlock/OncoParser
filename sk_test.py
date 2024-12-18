# import required module
from sklearn.feature_extraction.text import TfidfVectorizer
import pathlib
import ChapterParser

string = []
for file in pathlib.Path("Главы/").rglob("*.txt"):
    with open(file, "r", encoding="UTF-8") as f:
        string.extend(ChapterParser.splitOnParagraphs(f.read()))

# merge documents into a single corpus

# create object
tfidf = TfidfVectorizer()

# get tf-df values
result = tfidf.fit_transform(string)

# get idf values
print('\nidf values:')
for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
    print(ele1, ':', ele2)

# get indexing
print('\nWord indexes:')
print(tfidf.vocabulary_)

# display tf-idf values
print('\ntf-idf value:')
print(result)

# in matrix form
print('\ntf-idf values in matrix form:')
print(result.toarray())
