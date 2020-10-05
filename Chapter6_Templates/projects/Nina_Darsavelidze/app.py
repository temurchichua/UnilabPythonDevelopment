from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/page')
def page():
    image_list = ["https://archive.propaganda.network/uploads/artworks/gallery_1532684862.png", "https://archive.propaganda.network/uploads/artworks/gallery_1567762178.png", "https://archive.propaganda.network/uploads/artworks/gallery_1532684142.png"]
    return render_template('page.html', image_list=image_list)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/status')
def status():
    user_data = request.args
    first_name = user_data['first_name']
    last_name = user_data['last_name']
    return render_template('status.html', first_name=first_name, last_name=last_name)


app.run(debug=True)
