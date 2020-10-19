from flask import Flask, render_template, request
import string
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from datetime import datetime
import matplotlib
import os
import glob
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from nltk.stem.wordnet import WordNetLemmatizer
import shutil


lem = WordNetLemmatizer()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/report')
def report():
    raw_text = request.args.get('raw_text')

    def text_process(mess):
        """
        1. remove punc
        2. remove stop words
        3. return list of clean text words
        """

        nopunc = ''.join([char for char in mess if char not in string.punctuation])
        lem_words = []
        for word in word_tokenize(nopunc):
            lem_words.append(lem.lemmatize(word))

        return [word for word in lem_words if word not in stopwords.words('english')]

    clean_text = text_process(raw_text)
    word_freq = FreqDist(clean_text)
    word_freq.plot(10, title='Top 10 Most common Words in Text')
    now = datetime.now()
    plot_name=now.strftime("%d-%m-%Y-%H-%M-%S")+'.png'
    path='static/images/'

    files = glob.glob(path+'*')
    for items in files:
        os.remove(items)
    plt.savefig(path+plot_name)
    plt.close()

    return render_template('report.html', name='frequency distribution plot', url=path+plot_name)


if __name__ == '__main__':
    app.run(debug=True)
