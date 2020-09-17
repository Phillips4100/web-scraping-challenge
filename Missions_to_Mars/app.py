from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodg://localhost:27017/mars_app'
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = monfo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.replace_one({}, mars_data, upsert=True)
    return "Scrape Complete"

if __name__ == "__main__":
    app.run()