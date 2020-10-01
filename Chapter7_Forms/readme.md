# ფორმებთან მუშაობა Flask-ის დახმარებით

ამ თავში ვნახავთ თუ როგორ არის შესაძლებელი ფუნქციონალური ფორმების გამართვა ფლასკის მეშვეობით. ამაში WTForms დაგვეხმარება.
მანამდე კი გავეცნოთ მთავრ კომპონენტებს რომელსაც გამოვიყენებთ.
1. პირველ რიგში დავაყენებთ secret key-ს კონფირგურაციას უსაფრთხოებისთვის
2. შევქმნით WTForm კლასს
    - შევქმნით შესაბამის არეებს ფორმის თითოეული ნაწილისთვის
3. გავმართავთ View Function-ს
    - დავამატებთ მეთოდებს `methods = ['GET','POST']`
    - შევქმნით Form Class
    - დავამუშავებთ form submissionს

## სარჩევი
- [WTForms](#wtforms)
    - [ინსტალაცია](#wtforms-ინსტალაცია)
- [FlaskWTF](#flaskwtf)
    - [ინსტალაცია](#flaskwtf-ინსტალაცია)
    - [შესავალი](#შესავალი)
    - [ფორმის შექმნა](#ფორმის-შექმნა)
        - [Flask-ში აწყობილი ფორმის შაბლონთან დაკავშირება](#flask-მაგალითი)
- [Form Fields](#form-fields)

## [WTForms](https://wtforms.readthedocs.io/en/2.3.x/)
WTForms პითონში ვებ დეველოპმენტზე გათვლილი ფორმების ვალიდაციისა და რენდერის ბიბლიოთეკაა. ის თავსებადია ნებისმიერ ვებ ფრიმვორკთან ან ძრავის შაბლონთან. 
WTForms-ის გარშემო არის შექმნილი ბიბლიოთეკებიი რომელიც დაგვეხმარება ჩვენს არჩეულ ფრიმვორკში მის მოთავსებაში.
ერთ-ერთი რომელსაც ჩვენ გამოვიყენებთ და Flaskთან მუშაობაში დაგვეხმარება არის 

### [WTForms ინსტალაცია](https://pypi.org/project/WTForms/)
ბიბლიოთეკის ინსტალაცია შესაძლებელია [pip](http://www.pip-installer.org/) მენეჯერის გამოყენებით:

`pip install WTForms`

## [FlaskWTF](https://flask-wtf.readthedocs.io/en/stable/)
FlaskWTF არის Flask-ისა და WTForms-ის ინტეგრაცია, რომელიც აერთიანებს ისეთ შესაძლებლობებს როგორიცაა ფაილების ატვირთვა ან reCAPTCHA.

![FlaskWTF](https://flask-wtf.readthedocs.io/en/stable/_static/flask-wtf.png)

### [FlaskWTF ინსტალაცია](https://flask-wtf.readthedocs.io/en/stable/install.html)
ბიბლიოთეკის ინსტალაცია შესაძლებელია [pip](http://www.pip-installer.org/) მენეჯერის გამოყენებით:

`pip install Flask-WTF`

## [ფორმის შექმნა](https://flask-wtf.readthedocs.io/en/stable/form.html#creating-forms)
## [შესავალი](https://flask-wtf.readthedocs.io/en/stable/quickstart.html#creating-forms)
ბიბლიოთეკის გამოსაყენებლად უნდა შემოვიტანოთ შესაბამისი ბიბლიოთეკა აპლიკაციაში:
```python
from flask_wtf import FlaskForm
```

მოგვიანებით ვნახავთ როგორ უნდა გავუკეთოთ სტრუქტურიზაცია და ფაილ მენეჯმენტი პროექტში ფორმების შემცველ ფაილს.

ამის შემდგომ შეგვიძლია გამოვიყენოთ WTForms ბიბლიოთეკა შესაბამისი ფორმის შემოსატანად. მაგალითად სტრიგ მონაცემის ამოსაღები ფორმისთვის
შეგვიძლია გამოვიყენოთ `StringField`:

```python
from wtforms import StringField
```

როგორც ვახსენეთ პირველ საფეხური იქნება secret key. უსაფრთხოების შესაძლებლობების გამოსაყენებლად, მას შემდეგ რაც შევქმნით Flask app ობიექტს, შეგვიძლია კონფიგურაციაში გავუწეროთ Secret Key.

```python
app.config['SECRET_KEY'] = <Secret_Key>
```

მოგვიანებით ვნახავთ როგორ შეგვილია Secret Key მოვათავსოთ environmental ცვლადში მეტი დაცულობისთვის.

ამ ეტაპისთვის ჩვენი კოდი Flask და FlaskWTFთან ერთად, დაახლოებით ასე უნდა გამოიყურებოდეს (დამოკიდებულია თუ რა ელემენტები შემოგაქვთ ბიბლიოთეკებიდან).

```python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SEKRET_KEY'] = "Mellon"
```

### ერთეული ელემენტის მაგალითი

ფორმის ასაწყობად პითონში გამოვიყენებთ კლასებს და კლასების მემკვიდრულობის თვისებას. 
ყოველ ახალ ფორმას პარამეტრად გადავცემთ FlaskForm-ს რაც ამ კლასს ფორმის თვისებებს მიანიჭებს.

```python
class FormName(FlaskForm):
    information = StringField("What kind of information are you looking for?")
    submit = SubmitField('submit')
```

შეამჩნევდით რომ ფორმის ელემენტებს ისე ვქმნით როგორც კლასის ატრიბუტებს.

### Flask მაგალითი

ავაწყოთ ახალი როუთი რომელზეც გვსურს ფორმის გამოყენება.

```python
@app.route('/', methods=['GET', 'POST'])
def index():

    information = None

    form = FormName()

    if form.validate_on_submit():

        information = form.information.data
        form.information.data = ''

    return render_template('demo.html', form = form, information = information)

```

1. ვქმნილ როუთში ვქმნით ფორმის ობიექტს `form = FormName()`. 
2. `if form.validate_on_submit():` პირობით ვამოწმებთ მოთხოვნა ამ როუთზე
მოვიდა თუ არა ამ ფორმის დასაბმითებით
3. თუ ეს პირობა ჭეშმარიტია, გვეძლევა შესაძლებლობა ინფორმაციის ამოღების ფორმის ობიექტის შესაბამის ატრიბუტზე დატას ამოღებით 
`<form.attribute_name.data>`.
4. ამოღებულ ინფორმაციას გადავცემთ შაბლონს და ვტვირთავთ სრულ გვერდს `render_template()` მეთოდის გამოყენებით

##### საბოლოო Flask აპლიკაციის კოდი:

```python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = "Mellon"

class UsernameForm(FlaskForm):
    username = StringField("Username: ")
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def index():

    username = None

    form = UsernameForm()

    if form.validate_on_submit():

        username = form.username.data
        form.username.data = ''

    return render_template('demo.html', form = form, username = username)

if __name__ == '__main__':
    app.run(debug = True)
```

#### html-თან დაკავშირება - demo.html

```jinja2
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username() }}
        {{ form.submit() }}
    </form>
```

როგორც ხედავთ შემოტანილ form ობიექტის ატრიბუტებს ვიყენებთ ფორმის რენდერისათვის. საგულისხმოა რომ form ობიექი შეიცავს როგორც ჩვენს მიერ ხელით გაწერილ,
ისე FlaskForm კლასიდან მემკვიდრეობით მიღებულ ატრიბუტებს.

1. `{{ form.hidden_tag() }}` - FlaskForm კლასის ატრიბუტია და გვეხმარება ფორმის უსაფრთხოების გამართვაში
2. `{{ form.username.label }}` - მნიშვნელობად მიიღებს StringField-ისთვის გადაცემულ პირველ პარამეტრს, რომელიც გვინდოდა რომ ფორმის შევსებისას წარწერად გამოჩენილიყო
3. `{{ form.username() }}` - აგენერირებს უშუალოდ ფორმას შესაბამისი პარამეტრისთვის
4. `{{ form.submit() }}` - აგენერირებს საბმით ღილაკის ფორმას

## [Form Fields](https://wtforms.readthedocs.io/en/2.3.x/fields/)
### შესავალი
თითქმის ყველა [HTML form კლასს აქვს შესაბამისი WTForms კლასი](https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields) (და შესაბამისად FlaskWTF-ის მხარდაჭერა)
რომლის პროექტში შემოტანაც არის შესაძლებელი.
WTForms ასევე აქვს ვალიდატორიც რომლის ჩასმაც შესაძლებელია ფორმებში. ვალიდატორებს შეუძლიათ შეამოწმონ ფორმაში შეტანილი 
მონაცემი, მაგალითად ფორმატის მიხედვით, ან არის თუ არა შევსებული ფორმა და ა.შ.

ასევე ვნახავთ როგორ შეგვიძლია გამოვიყენოთ Flask-ის session ობიექტი რომ შევინახოთ ფორმიდან აღებული ინფორმაცია და გამოვიყენოთ
მოგვიანებით სხვა შაბლონზე მუშაობისას. მოგვიანებით კი შევძლებთ ამ ინფორმაციის სესიის მაგივრად მონაცემთა ბაზაში შენახვას.

გავამზადოთ სამუშაო გარემო და შემოვიტანოთ საჭირო ინსტრუმენტები:

```python
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
```