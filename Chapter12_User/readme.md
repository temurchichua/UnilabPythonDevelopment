# მომხმარებელი

## შესავალი

ამ დრომდე ჩვენს მიერ შექმნილ ყველა რესურსზე ღია წვდომა გვაქვს. ეს ნიშნავს რომ ნებისმიერი ვებ გვერდის თუ API-ს ფუნქციონალის ნახვა და გამოყენება ყველასთვის ღიაა. ხშირ შემთხვევაში კი გვჭირდება რომ გარკვეული ფუნქციონალი მხოლოდ რეგისტრირებული მომხმარებლისთვის გამოვაჩინოთ. შესაძლებელია რეგისტრირებული მომხმარებლებიც დავყოთ ქვეჯგუფებად და მივანიჭოთ მათ შესაბამისი პრივილეგიები და შესაძლებლობები. 

ამ თავის ძირითადი მისანია გავეცნოთ მომხმარებლის ავტორიზაციას და აუთენტიფიკაციას. პროცესში ვისწავლით პაროლის ჰაშირებას, ფლასკის აუტორიზაციის და აუტენთიფიკაციის ბიბლიოთეკების გამოყენებას.

## სარჩევი

[TOC]



## მომხმარებლის ავტორიზაცია და პაროლი

თუ საიტზე ვაპირებთ ავტორიზაციის ჩაშენებას ეს ნიშნავს, რომ მომხმარებელს შესაძლებლობას ვაძლევთ გაიაროს რეგისტრაცია და შექმნას თავისი ციფრული ანგარიში, რომელიც იქნება პერსონალურად მისი და რომლის დახმარებითაც შეძლებს გარკვეულ პროცესებზე მოიპოვოს წვდომა.

იმისთვის რომ მომხმარებლის ანგარიში დავიცვათ და ანგარიშის მართვაზე მხოლოდ მომხმარებელს ჰქონდეს წვდომა, საჭიროა გარკვეული ავტორიზაციის ფორმის გამოყენება. ყველაზე გავრცელებული ფორმა მომხმარებლის **უნიკალური იდენტიფიკატორისა** და მხოლოდ მისთვის ცნობილი **პაროლის** გამოყენებით ავტორიზაცია. ამ პროცესს log in ანუ შესვლის ფორმის გავლით გავდივართ.

ფორმაში შევსებული მონაცემის გადასამოწმებლად აუცილებელია სერვერის მხარესაც გვქონდეს შენახული მომხმარებლის მიერ რეგისტრაციის დროს არჩეული **იდენტიფიკატორი** (ხშირ შემთხვევაში *username*-მომხმარებლის სახელი) და პაროლი (password). რადგან მომხმარებლის პაროლი ერთ-ერთი ყველაზე ფაქიზი მონაცემია რაც მომხმარებლის მთელს ანგარიშზე წვდომის მოსაპოვებლად გამოიყენება, აუცილებელია მისი დაცვა შევძლოთ, იმ შემთხვევაშიც კი თუ ვინმე ჩვენი მონაცემთა ბაზიდან მონაცემის ამოღებას შეძლებს. შესაბამისად, უსაფრთხოების მიზნებისთვის, არასდროს არ უნდა შევინახოთ ტექსტი პირდაპირი სახით, იმ სტრინგად როგორც ის მომხმარებელმა შეავსო. 

ინფორმაციის დასაშიფრად შეგვიძლია გამოვიყენოთ **hash** ფუნქცია. ჰაშირება ნიშნავს ისეთი ალგორითმის გამოყენებას, რომელიც იღებს დოკუმენტს (ჩვენს შემთხვევაში პაროლის შიგთავსს) და უკან გვიბრუნებს უსაფრთხოდ დაშიფრულ ფაილს. ჰაშირებული ფაილი უსაფრთხოა რადგან ადამიანისთვის ამგვარი ფაილის შიგთავსი არაინტორმატიულია. საბედნიეროდ უკვე არსებობს ჰაშირების უამრავი სხვადასხვა ალგორითმი და ბიბლიოთეკა რომლის გამოყენებაც პროექტში შეგვიძლია.

შესაბამისად ჩვენ ჰაშირების ფუნქციის გამოყენებით დავშიფრავთ რეგისტრაციის დროს მომხმარებლის მიერ შეყვანილ პაროლს და ისე მოვათავსებთ მონაცემთა ბაზაში. მომხმარებლის ყოველი ავტორიზაციისას შეყვანილ პაროლსაც ანალგური ალგორითმით გავუკეთებთ ჰაშირებას და შევადარებთ მომხმარებლის იდენტიფიკატორის გასწვრივ დამახსოვრებულ ჰაშირებულ პაროლს. დამთხვევის შემთხვევაში შეგვიძლია ჩავთვალოთ რომ მომხმარებელმა ავტორიზაცია წარმატებით გაიარა.

ამისთვის ორი საკმაოდ გამოსადეგი ბიბლიოთეკები გვაქვს პითონ გარემოში, ჩვენ მათგან ორს განვიხილავთ. ესენია:

- Bcrypt
- Werkzeug

ორივე საკმაოდ პოპულარულია, ხშირად გამოიყენება Flask აპლიკაციებში და საკმაოდ ჰგავს ერთმანეთს. ასე რომ არჩევანი თქვენზეა, თუ რომელს გამოიყენებთ საბოლოოდ პროექტში.

## Bcrypt

<img src="https://i.ytimg.com/vi/r1Iygf-rRdE/maxresdefault.jpg" alt="Argon2 Password Hashing Node.js | BCrypt Alternative - YouTube" style="zoom:20%;" />

*bcrypt* არის პაროლის ჰაშირების ფუნქცია რომელიც Niels Provos და David Mazières დიზაინის მიხედვით შეიქმნა და გამოსაყენებლად 1999 გამოჩნდა, თუმცა დღემდე საკმაოდ აქტიურად გამოიყენება. მისი გამოყენება შესაძლებელია პითონის აპლიკაციებშიც, შესაბამისი ბიბლიოთეკის დაყენების შემდგომ:

```bash
pip install bcrypt
```

თუმცა ჩვენ გამოვიყენებთ უშუალოდ Flask-ზე ოპტიმიზირებულ ვერსიას, რომელსაც იოლად ჩავაშენებთ ჩვენს flask აპლიკაციაში:

```
 pip install flask-bcrypt
```

პროექტში შემოსატანად კი დგვჭირდება შემდეგი პითონის ინსტრუქციის გაწერა:

```python
from flask_bcrypt import Bcrypt
```

პროექტში Bycrpt-ის გამოსაყენებლად უნდა შევქმნათ შესაბამისი ჰეშერ ობიექტი. მისი დახმარებით შევძლებთ ნებისმიერი მონაცემის ჰაშირებას. ჰაშირების პროცესში დაგვეხმარება `generate_password_hash(password='string_to_hash')` მეთოდი.

მაგალითად:

```python
from flask_bcrypt import B crypt

bcrypt = Bcrypt()

password = "bestkeptsecret"

hashed_pass = bcrypt.generate_password_hash(password=password)

print(f'Hashed_Pass: {hashed_pass}')
```

დაგვიბრუნებს სტრინგის ჰაშირებულ ვერსიას:

` Hashed_Pass: b'$2b$12$m3DOb4ospynwqO.TEb6bHeJh3nWgenyRjpDA6LstfsjoOBpVzW3HG' `

ამრიგად დაშიფრული პაროლის შენახვა უკვე შესაძლებელია ბაზაში, რადგან როგორც ხედავთ ის ადამიანისთვის აბსოლუტურად არაინფორმატიულია.

მომხმარებლის მიერ შეყვანილი პაროლის გადასამოწმებლად, ისევ Bcrypt ბიბლიოთეკიდან გამოვიყენებთ `check_password_hash(hashed_pass, 'user_typed_password')`.  როგორც ხედავთ მეთოდს არგუმენტებად უნდა გადავცეთ შესადარებელი პარამეტრები. მეთოდი უკან დაგვიბრუნებს True/False მნიშვნელობებს იმის მიხედვით სწორია თუ არა მომხმარებლის შეყვანილი მონაცემი.

სრული რეფერენსისთვის ნახეთ [**მაგალითი**](/Chapter12_User/examples/bycrpt.py)

## Werkzeug

*werkzeug* German noun: “tool”. Etymology: *werk* (“work”), *zeug* (“stuff”)

![Werkzeug — Werkzeug Documentation (1.0.x)](https://werkzeug.palletsprojects.com/en/1.0.x/_static/werkzeug.png)

Werkzeug-ის გამოყენებაც იდენტურად ხდება. თუ ამ ეტაპზე არ გაქვთ ბიბლიოთეკა შეგიძლია გადმოწეროთ მენეჯერის დახმარებით:

`pip install Werkzeug` 

Werkzeug ხელსაწყოების ნაკლებია რომელიც იდეალურად მუშაობს Flask-თან ერთად, რადგან არ იყენებს გარე ბიბლიოთეკებს. 

ჩვებ განივუტებევთ მის secureity ნაკრებიდან პაროლის ჰაშირების ხელსაწყოებს: `generate_password_hash` და `check_password_hash`.

`from werkzeug.security import generate_password_hash, check_password_hash`

მნიშვნელოვანი განსხვავება `bcrypt`-ისგან არის რომ არ გვჭირდება დამატებითი ობიექქტის შექმნა ჰაშირების მეთოდების გამოსაყენებლად. ბიბლიოთეკიდან პირდაპირ შემოგვაქვს მეთოდები რომელიც ფუნქციისამებრ შეგვიძლია გამოვიყენოთ.

მაგალითად:

### პაროლის ჰაშირებისთვის

```python
hashed_pass = generate_password_hash('bestkeptsecret')
print(hashed_pass)
```

`Hashed_Pass: pbkdf2:sha256:150000$oFv3Q4NF$fe102689242d740cca5f1cd100c9bb3c31051c63a8df817f9a76dd26c49b6ceb`

### პაროლის შესამოწმებლად

```python
check = check_password_hash(hashed_pass, 'bestkeptsecret')
print(f'Result: {check}')
```

`Result: True`

## [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

`flask-login` არის ფლასკის დამატებითი ბიბლიოთეკა, რომელიც მომხმარებლის პროფილზე "შესვლის"/აუტენთიფიკაციის ფუნქციონალის ვებ აპლიკაციაში ჩაშენების საფეხურს გაგვიმარტივებს.  ის შედგება მარტივად გამოსაყენებელი დეკორეატორებისგან რომელითაც სწრაფად და იოლად ეწყობა მომხმარებლის სხვადასხვა ფუნქციონალი.

გარდა ავტორიზაციისა, Flask-login-ის გამოყენებით შესაძლებელია აქტიური მომხმარებლის სესიაში შენახვა, მომხმარებლის სესიის დაცვა რომ არ მოხდეს ინფორმაციის ქუქიებიდან ამოღება, გვერდებზე დაშვების კონტროლი ...

აპლიკაციაში ბიბლიოთეკის შესაძლებლობების გამოყენება ხდება [`LoginManager`](https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager) კლასის გამოყენებით. მისი დახმარებით შექმნილი ობიექტით ჩვენ შევძლებთ ბიბლიოთეკის ყველა ფუნქციონალზე წვდომის მოპოვებას:

```python
login_manager = LoginManager()
```

სწორედ მენეჯერი შეიცავს კოდს რომელიც გვეხმარება ჩვენი აპლიკაცია დავაკავშიროთ Flask-Login-თან, მომხმარებლის ამოცანებთან სამუშაოდ. როგორც ვთქვით ეს ასმოცანა შეძლება იყოს მომხმარებლის ვერიფიცირება, მომხმარებლის აღდგენა მისი იდენტიფიკატორით, ავტორიზებული მომხმარებლის გადამისამართება და ა.შ.

მას შემდეგ რაც flask აპლიკაციის ობიექტს შექმნით მისი დაკავშირება მენეჯერთან `init_app()` მეთოდით შეგვიძლია:

```
login_manager.init_app(app)
```

სტანდარტულად, Flask-Login  იყენებს სესიას მომხმარებლის ავტორიზაციისთვის. იმისთვის რომ მომხმარებლის ინფორმაცია დავიცვათ, აუცილებელია აპლიკაციას დავადოთ secret key, წინააღმდეგ შემთხვევაში ფლესკი დაგვიბრუნებს შეცდომის შეტყობინებას.

ამ კონფიგურაციის პროცესის სანახავად შეგიძლიათ შეამოწმოთ მაგალით [`__init__.py` მოდულში](#__init__.py)

*Warning:* Make SURE to use the given command in the “[How to generate good secret keys](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions)” section to generate your own secret key. DO NOT use the example one.

## სადემონსტრაციო პროექტის სტრუქტურა

დემონსტრაციისთვის ავაწყოთ ახალი აპლიკაცია. შესაბამისი სტრუქტურით:

```
FlaskApp
|____ myproject
|____ app.py
```

გაითვალისწინეთ, აპლიკაცია და პროექტის საქაღალდე ერთ დონეზეა.

myproject-ში დაგვჭირდება შესაბამისი ფაილების დამატება:

```
myproject
|____ __init__.py
|____ forms.py
|____ modules.py
|____ templates
     |____ base.html
     |____ home.html
     |____ login.html
     |____ register.html
     |____ welcome_user.html

```

### `__init__.py`

როგორც შევთანხმდით აქ ავაწყობთ აპლიკაციას და მის კონფიგურაციას

``` python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# შევქმნათ login manager ობიექტი
login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# გადავცეთ ჩვენი აპლიკაცია login_manager ობიექტს, init_app() მეთოდის გამოყენებით
login_manager.init_app(app)

# მივუთითოთ თუ რომელი view-დან შეძლებს მომხმარებელი საიტზე შესვლას
login_manager.login_view = "login"

```

### `models.py `

როგორც შევთანხმდით, ავტორიზაცია არის პროცესი, რომლის დროსაც რეგისტრირებული მომხმარებელი იდენტიფიკატორისა და პაროლის გამოყენებით ადასტურებს საკუთარ თავს. რეგისტრიებული მომხმარებელი ნიშნავს მომხმარებელს რომლის მონაცემებიც (მათ შორის ID და Password) დაცულია მონაცემთა ბაზაში. უკვე ვიცით რომ პაროლის დასაცავად ვშიფრავთ მას Hash ფუნქციით. მოდი შევაჯამოთ ყველა ეს დავალება და ვაქციოთ ის კოდად:

1. შევქმნათ ბაზის მოდელი რომელშიც მოვათავსებთ მომხმარებლის საბაზისო ინფორმაციას:
   1. მეილი
   2. იდენტიფიკატორი
   3. პაროლი
2. ობიექტის შენახვისას გავაკეთოთ პაროლის ჰაშირება
3. შევქმნათ check_password() მეთოდი, რომლითაც შეყვანილ პაროლს შევადარებთ ბაზასი არსებულს

#### 1. ბაზის მოდელის შექმნა

უკვე ვიცით რომ SQLAlchemy-ს დახმარებით ბაზის მოდელის შესაქმნელად გვესაჭიროება ბაზის ობიექტი. სწორედ მისი დახმარებით შეგვიძლია ვაქციოთ კლასი ბაზის მოდელად. შესაბამისად შემოვიტანოთ პროექტიდან `db` ობიექტი და გავწეროთ ბაზის მოდელი:

```python
from myproject import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
```

როგორც ხედავთ flask_login-იდან შემოვიტანეთ `UserMixin`. მისი დახმარებით მომხმარებლის უამრავ ატრიბუთან გვექნება წვდომა რომელიც ბიბლიოთეკაშია ჩაშენებული. `UserMixin`-ის პრაქტიკულ გამოყენებას შემდეგ საფეხურზე ვნახავთ.



#### 2. მომხმარებლის დამატება

`SQLAlchemy`-ის გამოყენებით, ბაზის მონაცემებთან ვმუშაობთ როგორც პითონის ობიექტებთან. პითონში კლასის მიხედვით ობიექტის ერთ-ერთი მარტივი გზა `__init__` მეთოდის გამოყენებაა. სწორედ ამ საფეხურზე, ობიექტის შექმნისას მოვახდენთ პაროლის ჰაშირებას, მის მონაცემთა საცავში ჩაწერამდე. ამისთვის გამოვიყენებ `werkzeug.security`-იდან ჰაშირების მეთოდს:

```python
from werkzeug.security import generate_password_hash,

# in class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
```

შესაბამისად ობიექტი, ანუ მწკრივი ბაზაში, შეიქმნება ჰაშირებული პაროლით. ამრიგად მომხმარებლის პაროლი ხდება დაცული.

#### 3. პაროლის გადამოწმების მეთოდი

პაროლის გადასამოწმებლად `werkzeug.security`-დან გამოვიყენებთ `check_password_hash()` მეთოდს:

```python
def check_password(self,password):
    return check_password_hash(self.password_hash,password)
```

#### შემოსული მომხმარებელი

მას შემდეგ რაც მომხმარებელი გაივლის ავტორიზაციას ჩვენ შეგვიძლია პროგრამის მსვლელობისას ამოვიღოთ ამ მომხმარებლის მონაცემი სხვადასხვა ამოცანებისთვის. მაგალითად ID, სახელი ან მომხმარებელთა ჯგუფი შეგვიძლია გამოვიყენოთ მომხმარებლის ვებ ვიუების შესაზღუდად ან დასაშვებად. 

ყველა ამ შესაძლებლობას, ფლასკის აპლიკაციით შექმნილი `login_manager` მოგცემს. შესაბასმისად ჩვენი პროექტიდან უნდა შემოვიტანოთ მენეჯერის ობიექტი. 

#####  [`user_loader`](https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager.user_loader)

`user_loader` გამოიყენება ავტორიზებული მომხმარებლის ჩასატვირთად. მისი გამოყენებით შეგვიძლია მონაცემთა ბაზიდან ამოვიღოთ მომხმარებლის ობიექტი, მისი ID-ს გამოყენებით. შესაბამისად უნდა ავაწყოთ ფუნქცია რომელსაც გადავცემთ მომხმარებლის იდენტიფიკატორს და დაგვიბრუნებს ამ იდენტიფიკატორის ქვეშ არსებული მომხმარებლის ობიექტს. ეს ყველაფერი კი უნდა შევმოსოთ `user_loader` დეკორატორით:

```python
from myproject import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
```

#### დასრულებული კოდი

საბოლოოდ თქვენს `models.py`-ს უნდა ჰქონდეს მსგავსი სტრუქტურული სახე. რა საკვირველია, ბაზის მოდელს შეგიძლიათ დაამატოთ ის სასურველი პარამეტრები, რომლის რეგისტრაციის დროს შეტანაც გსურთ მომხმარებლისგან ბაზაში. არ დაგავიწყდეთ რომ ამ პარამეტრების შესაბამისი ფორმა გაამზადოთ რეგისტრაციის გვერდზე გამოსაჩენად.

```python
from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
```

### forms.py

ამ თავში ავაწყობთ რეგისტრაციისა და ავტორიზაციის ფორმას. ასევე მოვამზადებთ ფუნქციებს მომხმარებლის მიერ შეყვანილი მონაცემების გადასამოწმებლად. პირველ რიგში შენივიტანოთ საჭირო ბიბლიოთეკები და ხელსაწყოები:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from myproject.models import User
```

ჩვენი ამოცანაა შევქმნათ სარეგისტრაციო ფორმების კლასები და გავწეროთ შესავსები ველების ელემენტები:

#### RegistrationForm

```python
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')
```

დააკვირდით რომ ვალიდატორები ფორმას გადაეცემა სიის სახით, იმ შემთხვევაშიც კი თუ ელემენტზე ვიყენებთ მხოლოდ ერთ ვალიდატორს.

რეგისტრაციის ფორმას გავუწერთ ორ ფუნქციონალს, რომელიც ფორმაში შევსებულ მონაცემს გადაამოწმებს. ესენია:

1. უკვე რეგისტრირებულია თუ არა მომხმარებლის სახელი
2. უკვე რეგისტრირებულია თუ არა მომხმარებლის ელექტრონული ფოსტა

###### `validate_email()`

მეთოდის მიზანია ფორმაში შევსებული იმეილი შეადაროს ბაზაში არსებულ ჩანაწერს. იმ შემთხვევაში თუ მონაცემი დაბრუნდება უნდა დავაბრუნოთ ვალიდაციის შეცდომა.

```python
def validate_email(self, email):
    if User.query.filter_by(email=self.email.data).first():
        raise ValidationError('Email has been registered')
```

###### `validate_username()`

```python
def validate_username(self, username):
    if User.query.filter_by(username=self.username.data).first():
        raise ValidationError('Username has been registered')
```

### app.py

დროა დავიწყოთ აპლიკაციის გამართვა და ფუნქციონალის ვიუების აწყობა. ამისთვის შემოვიტანოტ საჭირო ბიბლიოთეკები:

```python
from myproject import app,db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm
```

```python
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            # Log in the user

            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
```