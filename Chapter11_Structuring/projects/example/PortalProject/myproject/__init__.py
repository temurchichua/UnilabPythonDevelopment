import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# თუ კონფიგურაციისათვის იყენებთ ბევრ პარამეტრს სასურველია მათი config.py ფაილში გადანაწილება
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# გაითვალისწინე! აუცილებელია იმპორტების გაკეთება მას შემდეგ რაც db ობიექტს გაწერ
# წინააღმდეგ შემთხვევაში models.py დაგვიერორდება.
## ბაზასთან მომუშავე views.py ფაილები სათითაოდ შემოვიტანოთ მათი ბლუპრინტებით
from myproject.students.views import student_blueprint
from myproject.teachers.views import teachers_blueprint

app.register_blueprint(student_blueprint, url_prefix='/students' )
app.register_blueprint(teachers_blueprint, url_prefix='/teachers')
