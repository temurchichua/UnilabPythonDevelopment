import spacy
from spacy import  displacy
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("Today it was a good day, I was able to see some butterflies")

doc = nlp(text)

displacy.serve(doc, style="dep")
