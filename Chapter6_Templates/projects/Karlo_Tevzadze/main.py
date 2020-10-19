from flask import Flask, render_template,request
from flask_mail import Mail, Message
app = Flask(__name__)
mail= Mail(app)
app.config['SECRET_KEY'] = 'MrvlSecret'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mr.ktevzadze@gmail.com'
app.config['MAIL_PASSWORD'] = 'MrvlSecret'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/' )
def main():

    return render_template('index.html',title="Company Name")

@app.route('/index/<name>' )
def index(name):

    return render_template('index.html',name = name, title="Company Name")


@app.route('/about')
def about():
    return render_template('about.html',title="About")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    data = request.args
    user_name = data.get("first_name")
    user_last_name = data.get("last_name")
    user_mail = data.get("email")
    user_text = data.get("text")

    if user_text!=None:

        msg = Message(user_name, sender='mr.ktevzadze@gmail.com', recipients=['mr.ktvezadze@gmail.com',user_mail])
        msg.body = f"Dear {user_name},\n your mail({user_text})was successfully sent to the company mail.\n\nBest Regards,\nCarlo "
        msg.title = 'title'
        mail.send(msg)
    return render_template('contact.html',title='contact')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/success')
def success():
    data = request.args
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    return render_template('success.html', first_name = first_name, last_name = last_name)

app.run(port=5060, debug=True)