from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/game/<name>')
# def about(name):
#     my_list = ["isara", "shrek", "waldo"]
#     return render_template('about.html', name=name, my_list=my_list)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)
