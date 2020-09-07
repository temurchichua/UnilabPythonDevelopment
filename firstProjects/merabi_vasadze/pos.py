import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = "A spectre is haunting Europe — the spectre of communism."

doc = nlp(text)

displacy.render(doc, style="dep")
