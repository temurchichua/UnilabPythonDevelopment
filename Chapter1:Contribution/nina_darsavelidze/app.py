import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

text = """Blow-Up, his first English-language production, dives head-first into swinging London, seen from behind the wheel of a dandy photographer’s Rolls convertible – already, younger readers will be thinking of 
Austin Powers – as he bounces from slumming in a dosshouse to cavorting with dolly birds and models in his studio. There is a reason Antonioni has made the protagonist a photographer – a man who looks but doesn’t see – just 
as there was for replacing his original actor, Terence Stamp, with the relatively unknown David Hemmings."""

tokenized_text = word_tokenize(text)

for num, word in enumerate(tokenized_text):
    print(f"{num}-{word}")

tags = nltk.pos_tag(tokenized_text)

for num, tag in enumerate(tags):
    print(f"{num} word with tag - {tag}")


