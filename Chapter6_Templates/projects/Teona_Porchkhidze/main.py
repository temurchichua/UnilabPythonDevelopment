from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def drag_queen():
    return render_template("home.html")

@app.route("/cast")
def home():
    my_list=['Heidi N closet',"Jecky Fox","Gigi Goode","Crystal methyd","vidoo","jeyda essence hall","jen","Reiven"]

    
    
    return render_template("index.html",my_list=my_list)
if __name__ == '__main__':
    app.run(debug=True)
