from flask import Flask, render_template


app = Flask(__name__)


@app.route('/page')
def page():
    image_list = ["https://archive.propaganda.network/uploads/artworks/gallery_1532684862.png", "https://archive.propaganda.network/uploads/artworks/gallery_1567762178.png", "https://archive.propaganda.network/uploads/artworks/gallery_1532684142.png"]
    return render_template('page.html', image_list=image_list)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)


