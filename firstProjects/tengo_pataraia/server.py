from flask import Flask, render_template
import flask
import spacy
from spacy import displacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/',methods=["GET","POST"])
def process():

	if flask.request.method == "POST":
		text = flask.request.form["text"]

		text = nlp(text)

		svg = displacy.render(text,style="dep")

		return render_template('index.html',svg=svg)



if __name__ == '__main__':
   app.run()