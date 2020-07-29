# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
# -- Initialization section --
app = Flask(__name__)
city_names = ["new_york","san_francisco","atlanta","boston","baltimore","chicago","denver","detroit","honolulu","houston","la",",miami","washington-dc","seattle","austin","philadelphia"]
cities = {
    "la":{
        "city_name" : "Los Angeles",
        "med_household_income": 69150,
        "Car_costs" : 4.12,
        "Transit_costs" : 1.75
    },
    "boston":{
        "city_name" : "Boston",
        "med_household_income": 71834, 
        "Car_costs" : 2.64,
        "Transit_costs" : 2.75
    },
    "chicago":{
        "city_name" : "Chicago",
        "med_household_income": 57238, 
        "Car_costs" : 2.99,
        "Transit_costs" : "2.50"
    },
    "washington-dc":{
        "city_name" : "Washington DC",
        "med_household_income": 85203, 
        "Car_costs" : 2.61,
        "Transit_costs" : 2.25
    },
    "seattle":{
        "city_name" : "Seattle",
        "med_household_income": 92545,
        "Car_costs" : 3.55,
        "Transit_costs" : 2.25
    },
    "austin":{
        "city_name" : "Austin",
        "med_household_income": 55216, 
        "Car_costs" : 2.41,
        "Transit_costs" : 1.25
    },
    "miami":{
        "city_name" : "Miami",
        "med_household_income": 56328,
        "Car_costs" : 2.39,
        "Transit_costs" : 2.25
    },
    "houston":{
        "city_name" : "Houston",
        "med_household_income": 65394, 
        "Car_costs" : 2.25,
        "Transit_costs" : 1.25
    },
    "denver":{
        "city_name" : "Denver",
        "med_household_income": 68377, 
        "Car_costs" : 2.25,
        "Transit_costs" : "5.00"
    },
    "philadelphia":{
        "city_name" : "Philadelphia",
        "med_household_income": 46116, 
        "Car_costs" : 2.43,
        "Transit_costs" : "2.50"
    },
    "detroit":{
        "city_name" : "Detroit",
        "med_household_income": 26249,
        "Car_costs" : 2.92,
        "Transit_costs" : "1.50"
    },
    "atlanta":{
        "city_name" : "Atlanta",
        "med_household_income": 55279,
        "Car_costs" : 2.48,
        "Transit_costs" : "2.50"
    },
    "baltimore":{
        "city_name" : "Baltimore",
        "med_household_income": 75390, 
        "Car_costs" : "2.80",
        "Transit_costs" : "1.70"
    },
    "honolulu":{
        "city_name" : "Honolulu",
        "med_household_income": 60548, 
        "Car_costs" : 3.16,
        "Transit_costs" : 2.75
    },
    "san_francisco":{
        "city_name" : "San Fransciso",
        "med_household_income": 96265, 
        "Car_costs" : "3.10",
        "Transit_costs" : 2.75,
    },
    "new_york":{
        "city_name": "New York",
        "med_household_income" : 57782,
        "Car_costs" : 3.08,
        "Transit_costs" : 2.75,
    }
}
# -- Routes section --
@app.route('/')
@app.route('/index1')
def index_one():
    return render_template('index1.html')
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route("/")
@app. route("/san-francisco")
def san_fran(): 
    return render_template('san-francisco.html', city=cities["san_francisco"])
@app.route("/")
@app. route("/new-york")
def new_york(): 
    return render_template('new-york.html', city=cities["new_york"])
@app.route("/")
@app. route("/la")
def la():
    return render_template('la.html', city=cities["la"] )
@app.route("/")
@app. route("/boston")
def boston():
    return render_template('boston.html', city=cities["boston"])
@app.route("/")
@app. route("/chicago")
def chicago():
    return render_template('chicago.html', city=cities["chicago"])
@app.route("/")
@app. route("/washington-dc")
def washington_dc():
    return render_template('washington-dc.html', city=cities["washington-dc"])
@app.route("/")
@app. route("/seattle")
def seattle():
    return render_template('seattle.html', city=cities["seattle"])
@app.route("/")
@app. route("/austin")
def austin():
    return render_template('austin.html', city=cities["austin"])
@app.route("/")
@app. route("/miami")
def miami():
    return render_template('miami.html', city=cities["miami"])
@app.route("/")
@app. route("/denver")
def denver():
    return render_template('denver.html', city=cities["denver"])
@app.route("/")
@app. route("/philadelphia")
def philadelphia():
    return render_template('philadelphia.html', city=cities["philadelphia"])
@app.route("/")
@app. route("/detroit")
def detroit():
    return render_template('detroit.html', city=cities["detroit"])
@app.route("/")
@app. route("/atlanta")
def atlanta():
     return render_template('atlanta.html', city=cities["atlanta"])
@app.route("/")
@app. route("/baltimore")
def baltimore():
     return render_template('baltimore.html', city=cities["baltimore"])
@app.route("/")
@app. route("/honolulu")
def honolulu():
     return render_template('honolulu.html', city=cities["honolulu"])
@app.route("/")
@app. route("/houston")
def houston():
     return render_template('houston.html', city=cities["houston"])
