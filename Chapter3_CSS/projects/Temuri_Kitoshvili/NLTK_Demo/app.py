from flask import Flask, render_template, request
import nltk
from nltk.tokenize import sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

tokenizer = nltk.RegexpTokenizer(r"\w+")
lem=WordNetLemmatizer()
stopWords = set(stopwords.words("english"))



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])




def home():
    if (request.method == 'POST'):
        textName = request.form['textName']
        text = request.form['text']
        devideSentences = request.form.get('devideSentences')
        freqDist = request.form.get('freqDist')
        number = 0
        if freqDist != None:
            number = request.form['number']

        sentences = sent_tokenize(text)
        clean_sentences = []

        if (devideSentences=="on"):

            for num, sent in enumerate(sentences):
                clear_sentence = tokenizer.tokenize(sent)
                clear_sentence_str = ' '.join([str(elem) for elem in clear_sentence])
                clean_sentences.append(clear_sentence_str)

        freq_dist = ''
        if (freqDist=="on"):
            clean = []
            filtered_words = []
            for num, sent in enumerate(sentences):
                clear_sentence = tokenizer.tokenize(sent)
                clean.append(clear_sentence)

            for sent in clean:
                for word in sent:
                    words = lem.lemmatize(word, "v")
                    if words not in stopWords:
                        filtered_words.append(word)
            dist = FreqDist(filtered_words)
            freq_dist = dist.most_common(int(number))




        return render_template('analyse.html', textName=textName, text=text, clean_sentences=clean_sentences, freq_dist=freq_dist)

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)