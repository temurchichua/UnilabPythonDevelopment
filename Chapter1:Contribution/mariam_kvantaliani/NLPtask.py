import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, treebank_chunk
from nltk.stem import WordNetLemmatizer
import spacy
from nltk import tag, chunk, Tree


#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('treebank')

text = """ NASA was established in 1958, succeeding the National Advisory Committee for Aeronautics (NACA). The new agency was to have a distinctly civilian orientation, encouraging peaceful applications in space science.Since its establishment, most US space exploration efforts have been led by NASA, including the Apollo Moon landing missions, the Skylab space station, and later the Space Shuttle. NASA is supporting the International Space Station and is overseeing the development of the Orion spacecraft, the Space Launch System, and Commercial Crew vehicles. The agency is also responsible for the Launch Services Program, which provides oversight of launch operations and countdown management for uncrewed NASA launches. """

# პარაგრაფის წინადადებებად დაყოფა

sent_result = sent_tokenize(text)

# for num, sentence in enumerate(sent_result):
#     print(f'{num}. {sentence}')

# წინადადების სიტყვებად დანაწევრება

word_result = word_tokenize(text)

# for num, word in enumerate(word_result):
#     print(f'{num}. {word}')

# remove all tokens that are not alphabet

words = [word for word in word_result if word.isalpha()]
# print(words)

# clean full text from spot_words

stop_words = set(stopwords.words('english'))
text_result = [t for t in words if not t in stop_words]
#print(text_result) 

# lemmatization of text_result

lemmatizer = WordNetLemmatizer()
lemmatized_output = [lemmatizer.lemmatize(w, 'v') for w in text_result]
#print(lemmatized_output)

# spacy
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# for entity in doc.ents:
#     print(entity.text, entity.label_)


# create treebank
# 1. word tokenizarion
print(sent_result[0])
sent = word_tokenize(sent_result[0])

# 2. POS Tagging
tagged_sent = tag.pos_tag(sent)
#print(tagged_sent)

# 3. NE Chunking
# tree = chunk.ne_chunk(tagged_sent)
#tree.draw()

# treebank Corpus

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(tagged_sent)
print(result)
result.draw()
