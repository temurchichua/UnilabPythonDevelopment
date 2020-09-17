import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import treebank

# nltk.download('maxent_ne_chunker')
# nltk.download('words')

nltk.download('treebank')

sentence = "There's a bluebird in my heart that wants to get out but I'm too tough"

tokens = word_tokenize(sentence)

tags = nltk.pos_tag(tokens)

entities = nltk.chunk.ne_chunk(tags)

t = treebank.parsed_sents('wsj_001.mrg')[0]

t.draw()


