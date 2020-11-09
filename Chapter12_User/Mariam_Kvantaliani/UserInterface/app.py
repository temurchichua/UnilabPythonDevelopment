from project import app, db
from flask import render_template, redirect, request, url_for, flash, abort

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)