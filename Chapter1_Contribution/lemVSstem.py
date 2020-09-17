from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()

word = 'flying'
stemmed = stem.stem(word)

print(f'Lemmatized Word: {lem.lemmatize(word, "v")}')
print(f'Stemmed Word: {stemmed}')

