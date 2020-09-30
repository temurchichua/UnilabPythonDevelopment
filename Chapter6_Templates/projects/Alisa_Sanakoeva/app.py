from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about/<pet>')
def about(pet):
    return render_template('about.html', pet=pet)

app.run(port=4000, debug=True)