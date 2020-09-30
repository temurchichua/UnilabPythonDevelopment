from flask import Flask, render_template

app = Flask(__name__)
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

@app.route('/contact')
def contact():

    return render_template('contact.html',title="Contact")





app.run(debug=True,port=5000)
