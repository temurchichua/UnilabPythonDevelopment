import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words("english"))

ps = PorterStemmer()

text = '''There's a bluebird in my heart
That wants to get out but I'm too tough
I say: "Stay in there
I'm not going to let anybody see"
There's a bluebird in my heart
That wants to get out but I pour whiskey
I take a cigarette so the whores
The bartenders, the grocery clerks
Never know that he is in there
There's a bluebird in my heart
That wants to get out but I'm too tough
I say: "Stay down
Do you wanna mess me up?
Do you wanna screw up all of my works?"'''

# sent_result = sent_tokenize(text)
word_result = word_tokenize(text) # word_result holds the tokenized text of words

filtered_sentences = []

for word in word_result:
    if word not in stop_words:
        filtered_sentences.append(word)

stemmed_word = []

for word in filtered_sentences:
    stemmed_word.append(ps.stem(word))


# print(f'Tokenization Result: {word_result}')
print(f'Filtered Result: {filtered_sentences}')
print(f'Stemmed Result: {stemmed_word}')

# sentence = sent_result[1]
#
# print(f'sentence: {sentence}')


# for num, word in enumerate(word_result):
#     print(f'{num}. {word}')

# fdist = FreqDist(word_result)
#
# fdist.plot(15)
#
# plt.show()

