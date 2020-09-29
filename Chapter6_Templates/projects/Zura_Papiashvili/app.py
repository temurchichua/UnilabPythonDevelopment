from flask import Flask, render_template,request
from flask_mail import Mail, Message
app = Flask(__name__)
mail= Mail(app)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'papiashvil@gmail.com'
app.config['MAIL_PASSWORD'] = 'fsdqudsdyqcvxrch'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/' )
def index():

    return render_template('index.html',title="Company Name")

@app.route('/home',methods=['GET','POST'])
def home():
    ecolist=['Chemical Abstracts', 'U.S.A.SCOPUS','EBSCO Publishing', 'U.S.A.Cambridge Science Abstracts','Ecology Abstracts','Pollution Abstracts',
                            'Eco-Disc CD Rom','Geological Abstracts','International Development Abstracts','Oceanographic Literature Review','Zoological Records',
             'Indian Science Abstracts', 'Niscair', 'IndiaElsevier’s Compendex','Elsevier’s Current Awareness in Biological Sciences',
                                                                                'Elsevier’s Encompass','Elsevier’s Geobase']


    return render_template('home.html',title = "Home",ecolist=ecolist)

@app.route('/about')
def about():

    return render_template('about.html',title="About")




@app.route('/success')
def success():
    data = request.args
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    return render_template('success.html', first_name = first_name, last_name = last_name)



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    data = request.args
    user_name = data.get("first_name")
    user_last_name = data.get("last_name")
    user_mail = data.get("email")
    user_text = data.get("text")

    if user_text!=None:
        # Grab the user from our User Models table

        msg = Message(user_name, sender='papiashvil@gmail.com', recipients=['papiashvil@gmail.com',user_mail])
        msg.body = f"Dear {user_name},\n your mail({user_text})was successfully sent to the company mail.\n\nBest Regards,\nZura "
        msg.title = 'title'
        mail.send(msg)
    return render_template('contact.html',title='contact')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template('registration.html')





app.run(debug=True,port=5000)
