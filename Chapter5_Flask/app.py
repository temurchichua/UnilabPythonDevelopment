from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>გამარჯობა</h1>"

@app.route('/about')
def about():
    return "<h1>კომპანიის სახელია </h1>"
####
@app.route('/user/<username>', methods=['GET'])
def user_info(username):
    return f"<h1>ინფორმაცია მომხმარებელზე:  {username}</h1>"


@app.route('/post/<int:post_id>')
def post_info(post_id):

    return f'post_id: {post_id.split("/")[0]} .'

@app.route('/randompage')
def write_user_info():
    return 'თქვენ იმყოფებით შემთხვევით გვერდზე'
####
app.run(port=5005, debug=True)

