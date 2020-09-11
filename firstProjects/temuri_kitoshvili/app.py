import nltk
from nltk.tokenize import sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

tokenizer = nltk.RegexpTokenizer(r"\w+")
lem=WordNetLemmatizer()
stopWords = set(stopwords.words("english"))


text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# ტექსტის წინადადებებად დაშლა
sentences = sent_tokenize(text)

# წინადადებები სასვენი ნიშნების გარეშე
clean_sentences = []

# ტექსტის აშორებს სასვენ ნიშნებს და ყოფს წინადადებებად
def cleanSentences(sentence):
    for num, sent in enumerate(sentences):
        clear_sentence = tokenizer.tokenize(sent)
        clean_sentences.append(clear_sentence)
        # print(clear_sentence)

cleanSentences(sentences)


# აგებს დამოკიდებულების ხეს
def wordTree(clean_sentences):
    for sent in clean_sentences:
        # POS tagging
        tagged_sent = nltk.pos_tag(sent)
        # print(tagged_sent)

        # entities
        entities = nltk.chunk.ne_chunk(tagged_sent)
        entities.draw()

# wordTree(clean_sentences)


# აკეთებს ლემატიზირებული სიტყვების სიას
lemmatize_words = []

def lematizator(clean_sentences):
    for sent in clean_sentences:
        for word in sent:
            words = lem.lemmatize(word, "v")
            lemmatize_words.append(words)

lematizator(clean_sentences)



# ლემატიზირებული სიტყვების სიიდან იღებს stopword-ებს და აგებს სიხშირის განაწილებას
filtered_words = []
def dist(lemmatize_words):
    for word in lemmatize_words:
        if word not in stopWords:
            filtered_words.append(word)

    dist = FreqDist(filtered_words)
    # print(dist.most_common(5))

dist(lemmatize_words)


# წინადადებებში გვინიშნავს საკუთარ არსებით სახელებს და ზმნას
def wordsWithParram(clean_sentences):
    for word in clean_sentences:
        tagged_sent = nltk.pos_tag(word)

        chunkGram = r"""Chunk: {<VB.?>*<NNP>?} """
        chuckParser = nltk.RegexpParser(chunkGram)
        chunked = chuckParser.parse(tagged_sent)

        chunked.draw()

wordsWithParram(clean_sentences)




