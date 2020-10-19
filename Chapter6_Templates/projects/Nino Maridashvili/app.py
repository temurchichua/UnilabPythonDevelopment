from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/registered')
def registered():
    data = request.args
    username = data.get('username')
    return render_template('registered.html', username = username)

@app.route('/choose')
def choose():
    return render_template('choose.html')



app.run(debug=True)
