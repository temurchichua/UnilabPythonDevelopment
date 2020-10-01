from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about/<pet>')
def about(pet):
    return render_template('about.html', pet=pet)

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/status')
def status():
    data = request.args
    username = data.get("username")
    return render_template('status.html', username=username)


app.run(port=4000, debug=True)