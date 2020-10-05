from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/success')  
def success():
    data = request.args

    first_name = data.get('first_name')
    last_name = data.get('last_name')

    return render_template('success.html', first_name = first_name, last_name = last_name)

app.run(debug=True)

def some_function():
    pass
