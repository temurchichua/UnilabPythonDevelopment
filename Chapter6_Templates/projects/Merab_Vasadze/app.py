from flask import Flask,  render_template


app = Flask(__name__)


@app.route('/0AD/<name>')
def home(name):
    my_list = [("Jonas", "Adam"), ("Martha", "Eva"), ("Hanno", "Noah")]
    return render_template('Dark.html', name=name, my_list=my_list)


app.run(port=5000, debug=True)
