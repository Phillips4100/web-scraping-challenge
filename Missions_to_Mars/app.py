from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/marsDB'
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data=mongo.db.mars.find_one()
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrape():
    all_data=scrape_mars.scrape_all()
    mongo.db.mars.update({}, all_data, upsert=True)
    return redirect('/')

if __name__ == "__main__":
    app.run()
