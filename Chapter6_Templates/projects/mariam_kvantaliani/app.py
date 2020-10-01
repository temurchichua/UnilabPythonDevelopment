from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/book')
def book():
    return render_template('book.html')


@app.route('/image')
def image():
    return render_template('image.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/success')
def success():
    data = request.args
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    return render_template('success.html', first_name = first_name, last_name = last_name)

@app.route('/text')
def text():
    data = request.args
    text_name = data.get('text_name')
    return render_template('text.html', text_name = text_name)

app.run(debug=True)