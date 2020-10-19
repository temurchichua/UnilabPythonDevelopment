from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/generals')
def generals():
    return render_template('generals.html')


@app.route('/home')
def home():
    return render_template('home.html')


app.run(port=5000, debug=True)
