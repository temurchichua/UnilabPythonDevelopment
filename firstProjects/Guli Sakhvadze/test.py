import spacy
from spacy import displacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_sm")
text = nlp('''Kraftwerk is a German band formed in Düsseldorf in 1970 by Ralf Hütter and Florian Schneider. Widely considered as innovators and pioneers of electronic music, they were among the first successful acts to popularize the genre.''')


# FILTERS OUT STOP WORDS
#print(STOP_WORDS) #prints all the stop words
#STOP_WORDS.add("lol") #adds "lol" as a stop word


nostops = []
for word in text:
    if word.is_stop == False and word.is_punct == False:
        nostops.append(word)
print(nostops)
print("\n")


# PRINTS EACH WORD FROM nostops
#for word in nostops:
#    print(word.text)


# ADDS .pos_ .dep_ ATTRIBUTE
for word in text:
    print(word.text,  word.pos_, word.dep_)
#spacy.explain('advmod')

# VISUALIZES WORDS DEPENDENCY | HAS VISUALIZER OPTIONS (color, font, etc.) | SHOWS LEMMATIZED FORM OF THE WORDS
options = {'compact':True, 'bg':'#C0C0C0','color':'#000000', 'font':'Sans Serif', 'add_lemma':True}
displacy.serve(text, style="dep", options = options)


# SHOWS HOW CLOSE TWO WORDS ARE SEMANTICALLY
#for word1 in nostops:
#    for word2 in nostops:
#        print((word1.text, word2.text), "SImilarity is: ", word1.similarity(word2))
