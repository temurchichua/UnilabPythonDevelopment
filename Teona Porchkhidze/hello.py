#nltk- შესაძლებლობების გატესტვა

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy

#მიზანი - ტექსტის წინადადებებად და წინადადებების სიტყვებად დაყოფა

example_text="Musk has stated that he does not believe the U.S. government should provide subsidies to companies but should instead use a carbon tax to price in the negative externality of climate change and discourage poor behavior. Musk says that the free market would achieve the best solution, and that producing environmentally unfriendly vehicles should come with its own consequences."

# for number, sentence in enumerate(sent_tokenize(example_text)):
#     print(f'{number}. {sentence}')
#
# for i in word_tokenize(example_text):
#     print(i)

#მიზანი - stop words მოშორება ტექსტიდან.
stop = set(stopwords.words('english'))
# print(stop) ყველა სტოპ ვორდები რაც არსებობს ინგლისურში

# free_sent=[]

# for word in word_tokenize(example_text):
#     if word not in stop:
#         free_sent.append(word)
#
# print(free_sent)

#WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

# print(lemmatizer.lemmatize("better",pos="a"))

#spacy

nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)



