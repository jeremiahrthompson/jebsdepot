from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/jebsdepot-main"
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<username>")
def user_profile(username):
    user = mongo.db.jebsdepot_collection.find_one({"username": username})
    return render_template("user.html", user=user)
