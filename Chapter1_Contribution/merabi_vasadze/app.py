import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from firstrepo.firstProjects.merabi_vasadze.texttolemmatize import text

# nltk.download()
stop_words = set(stopwords.words("english"))

lem = WordNetLemmatizer()

text1 = "i was going in cafe, with my friends Jacob, fly"

word_result = word_tokenize(text1)

filtered_words = list(filter(lambda word: word not in stop_words, word_result))

print(filtered_words)
print(lemmed_word)

fdist = FreqDist(lemmed_word)

print(fdist.most_common(10))
