import email
from random import randint,seed
from operator import index
from unicodedata import name
import numpy as np
from joblib import load
from flask import Flask,render_template
from INPUT import Predict
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost:3306/GDP_capita1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
seed(1)

class GDP_Feature(db.Model):
    key=db.Column(db.Integer,primary_key=True)
    Popu=db.Column(db.Float,index=True)
    Area=db.Column(db.Float,index=True)
    Coastline=db.Column(db.Float,index=True)
    Net_migr=db.Column(db.Float,index=True)
    Infant=db.Column(db.Float,index=True)
    Litracy=db.Column(db.Float,index=True)
    Phones=db.Column(db.Float,index=True)
    Crops=db.Column(db.Float,index=True)
    Others=db.Column(db.Float,index=True)
    birthrate=db.Column(db.Float,index=True)
    agriculture=db.Column(db.Float,index=True)
    region=db.Column(db.String(50),index=True)
    country=db.Column(db.String(50),index=True)
    pred=db.Column(db.Float,index=True)
    def __init__(self,key,Popu,Area,Coastline,Net_migr,Infant,Litracy,Phones,Crops,Others,birthrate,agriculture,region,country,pred) :
        self.key=key
        self.Popu=Popu
        self.Area=Area
        self.Coastline=Coastline
        self.Net_migr=Net_migr
        self.Infant=Infant
        self.Litracy=Litracy
        self.Phones=Phones
        self.Crops=Crops
        self.Others=Others
        self.birthrate=birthrate
        self.agriculture=agriculture
        self.region=region
        self.country=country
        self.pred=pred
db.create_all()

@app.route('/')
def Home():
    return render_template("index.html")


@app.route('/Prediction',methods=["GET","POST"])
def Prediction():
    Form=Predict()

    if Form.validate_on_submit():
        list1 = []
        Population=Form.Population.data
        Area=Form.Area.data
        Coastline=Form.Coastline.data

        Net_migration=Form.Net_migration.data
        Infant=Form.Infant_mortality.data
        Litracy=Form.Litracy.data
        Phones=Form.Phones.data
        Crops=Form.Crops.data
        Other=Form.Other.data
        Birthrate=Form.Birthrate.data
        Agriculture=Form.Agriculture.data
        population=float(Population)
        list1.append(population)
        area=float(Area)
        list1.append(area)
        coastline=float(Coastline)
        list1.append(coastline)
        net_migration=float(Net_migration)
        list1.append(net_migration)
        IF=float(Infant)
        list1.append(IF)
        litracy=float(Litracy)
        list1.append(litracy)
        phone=float(Phones)
        list1.append(phone)
        crops=float(Crops)
        list1.append(crops)
        other=float(Other)
        list1.append(other)
        birthrate=float(Birthrate)
        list1.append(birthrate)
        agriculture=float(Agriculture)
        list1.append(agriculture)
        region=Form.Region.data
        if (region == 'Region_ASIA (EX. NEAR EAST)'):
            list1.append(1)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
        if (region =='Region_BALTICS'):
            list1.append(0)
            list1.append(1)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
        if (region == 'Region_C.W. OF IND. STATES'):
            list1.append(0)
            list1.append(0)
            list1.append(1)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
        if (region == 'Region_EASTERN EUROPE'):
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(1)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
        if (region == 'Region_LATIN AMER. & CARIB'):
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(1)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
        if (region == 'Region_NEAR EAST)'):
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(1)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
        if (region == 'Region_NORTHERN AFRICA '):
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(1)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
        if (region == 'Region_NORTHERN AMERICA'):
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(1)
            list1.append(0)
            list1.append(0)
            list1.append(0)
        if (region == 'Region_OCEANIA'):
            list1.append(1)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(1)
            list1.append(0)
            list1.append(0)
        if (region == 'Region_SUB-SAHARAN AFRICA '):
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(1)
            list1.append(0)
        if (region == 'Region_WESTERN EUROPE'):
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(0)
            list1.append(1)
        country=Form.Country.data
        list1.append(country)
        data=[np.array(list1)]
        model=load('GDP_per_capita_prediction.joblib')
        prediction=model.predict(data)

  

        COUNT_dict = {'Afghanistan': 0, 'Albania': 1, 'Algeria': 2,
              'American Samoa': 3, 'Andorra': 4, 'Angola': 5,
              'Anguilla': 6, 'Antigua & Barbuda': 7, 'Argentina': 8,
              'Armenia': 9, 'Aruba': 10, 'Australia': 11, 'Austria': 12, 'Azerbaijan': 13,
              'Bahamas, The': 14, 'Bahrain': 15, 'Bangladesh': 16, 'Barbados': 17,
              'Belarus': 18, 'Belgium': 19, 'Belize': 20, 'Benin': 21, 'Bermuda': 22,
              'Bhutan': 23, 'Bolivia': 24, 'Bosnia & Herzegovina': 25, 'Botswana': 26,
              'Brazil': 27, 'British Virgin Is.': 28, 'Brunei': 29, 'Bulgaria': 30,
              'Burkina Faso': 31, 'Burma': 32, 'Burundi': 33, 'Cambodia': 34,
              'Cameroon': 35, 'Canada': 36, 'Cape Verde': 37, 'Cayman Islands': 38,
              'Central African Rep.': 39, 'Chad': 40, 'Chile': 41, 'China': 42,
              'Colombia': 43, 'Comoros': 44, 'Congo, Dem. Rep.': 45,
              'Congo, Repub. of the': 46, 'Cook Islands': 47, 'Costa Rica': 48,
              "Cote d'Ivoire": 49, 'Croatia': 50, 'Cuba': 51, 'Cyprus': 52,
              'Czech Republic': 53, 'Denmark': 54, 'Djibouti': 55, 'Dominica': 56,
              'Dominican Republic': 57, 'East Timor': 58, 'Ecuador': 59, 'Egypt': 60,
              'El Salvador': 61, 'Equatorial Guinea': 62, 'Eritrea': 63, 'Estonia': 64,
              'Ethiopia': 65, 'Faroe Islands': 66, 'Fiji': 67, 'Finland': 68, 'France': 69,
              'French Guiana': 70, 'French Polynesia': 71, 'Gabon': 72, 'Gambia, The': 73,
              'Gaza Strip': 74, 'Georgia': 75, 'Germany': 76, 'Ghana': 77, 'Gibraltar': 78,
              'Greece': 79, 'Greenland': 80, 'Grenada': 81, 'Guadeloupe': 82, 'Guam': 83,
              'Guatemala': 84, 'Guernsey': 85, 'Guinea': 86, 'Guinea-Bissau': 87, 'Guyana': 88,
              'Haiti': 89, 'Honduras': 90, 'Hong Kong': 91, 'Hungary': 92, 'Iceland': 93,
              'India': 94, 'Indonesia': 95, 'Iran': 96, 'Iraq': 97, 'Ireland': 98,
              'Isle of Man': 99, 'Israel': 100, 'Italy': 101, 'Jamaica': 102, 'Japan': 103,
              'Jersey': 104, 'Jordan': 105, 'Kazakhstan': 106, 'Kenya': 107, 'Kiribati': 108, 'Korea, North': 109,
              'Korea, South': 110, 'Kuwait': 111, 'Kyrgyzstan': 112, 'Laos': 113, 'Latvia': 114,
              'Lebanon': 115, 'Lesotho': 116, 'Liberia': 117, 'Libya': 118, 'Liechtenstein': 119,
              'Lithuania': 120, 'Luxembourg': 121, 'Macau': 122, 'Macedonia': 123,
              'Madagascar': 124, 'Malawi': 125, 'Malaysia': 126, 'Maldives': 127,
              'Mali': 128, 'Malta': 129, 'Marshall Islands': 130, 'Martinique': 131,
              'Mauritania': 132, 'Mauritius': 133, 'Mayotte': 134, 'Mexico': 135,
              'Micronesia, Fed. St.': 136, 'Moldova': 137, 'Monaco': 138, 'Mongolia': 139,
              'Montserrat': 140, 'Morocco': 141, 'Mozambique': 142, 'Namibia': 143,
              'Nauru': 144, 'Nepal': 145, 'Netherlands': 146, 'Netherlands Antilles': 147,
              'New Caledonia': 148, 'New Zealand': 149, 'Nicaragua': 150, 'Niger': 151,
              'Nigeria': 152, 'N. Mariana Islands': 153, 'Norway': 154, 'Oman': 155,
              'Pakistan': 156, 'Palau': 157, 'Panama': 158, 'Papua New Guinea': 159,
              'Paraguay': 160, 'Peru': 161, 'Philippines': 162, 'Poland': 163,
              'Portugal': 164, 'Puerto Rico': 165, 'Qatar': 166, 'Reunion': 167,
              'Romania': 168, 'Russia': 169, 'Rwanda': 170, 'Saint Helena': 171,
              'Saint Kitts & Nevis': 172, 'Saint Lucia': 173, 'St Pierre & Miquelon': 174,
              'Saint Vincent and the Grenadines': 175, 'Samoa': 176, 'San Marino': 177,
              'Sao Tome & Principe': 178, 'Saudi Arabia': 179, 'Senegal': 180, 'Serbia': 181, 'Seychelles': 182,
              'Sierra Leone': 183, 'Singapore': 184, 'Slovakia': 185, 'Slovenia': 186,
              'Solomon Islands': 187, 'Somalia': 188, 'South Africa': 189, 'Spain': 190,
              'Sri Lanka': 191, 'Sudan': 192, 'Suriname': 193, 'Swaziland': 194, 'Sweden': 195,
              'Switzerland': 196, 'Syria': 197, 'Taiwan': 198, 'Tajikistan': 199, 'Tanzania': 200, 'Thailand': 201,
              'Togo': 202, 'Tonga': 203, 'Trinidad & Tobago': 204, 'Tunisia': 205, 'Turkey': 206,
              'Turkmenistan': 207,
              'Turks & Caicos Is': 208, 'Tuvalu': 209, 'Uganda': 210, 'Ukraine': 211, 'United Arab Emirates': 212,
              'United Kingdom': 213, 'United States': 214, 'Uruguay': 215, 'Uzbekistan': 216,
              'Vanuatu': 217, 'Venezuela': 218, 'Vietnam': 219, 'Virgin Islands': 220,
              'Wallis and Futuna': 221, 'West Bank': 222, 'Western Sahara': 223, 'Yemen': 224,
              'Zambia': 225, 'Zimbabwe': 226}
        key_list=list(COUNT_dict.keys())
        country=int(country)
        value=randint(0,10000)
        c_name=key_list[country]
        country=country+value
        gdp=GDP_Feature(country,population,area,coastline,net_migration,IF,litracy,phone,crops,other,birthrate,agriculture,region,c_name,prediction[0])
        db.session.add(gdp)
        db.session.commit()
        return render_template('Answer.html',prediction=prediction,c_name=c_name)
    return render_template("prediction.html",Form=Form)
@app.route('/About')
def About():
    return render_template("about.html")
@app.route('/Analysis')
def Analysis():
    return render_template("analysis.html")
@app.route('/Contact')
def Contact():
    return render_template("contact.html")

if __name__=='__main__':
    app.run(debug=True)
    
    