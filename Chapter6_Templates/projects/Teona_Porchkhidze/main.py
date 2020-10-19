from flask import Flask,render_template,url_for

app=Flask(__name__,static_folder='static')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cast")
def about():
    my_list=['Heidi N closet',"Jecky Fox","Gigi Goode","Crystal methyd","vidoo","jeyda essence hall","jen","Reiven"]

    
    return render_template("index.html",my_list=my_list)


@app.route("/werk")
def werk():
    return render_template("werk.html")


@app.route("/drag")
def drag():
    return render_template("test.html")


@app.route("/registration")
def registration():
    return render_template("test.html")




if __name__ == '__main__':
    app.run(debug=True)

