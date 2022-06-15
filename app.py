from flask import Flask, render_template,request
app = Flask(__name__)
import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://admin:2LlSMHZHg6axsock@cluster0.2vhzr6w.mongodb.net/?retryWrites=true&w=majority")
db = client["db"]
collection = db.get_collection("users")

list3 = ["dd","ss","aa"]


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        filterBolde = { 'name': request.form["bolde"] }
        filterDunke = { 'name': request.form["dunke"] }
        newvaluesForBolde = { "$set": { 'bolde': datetime.datetime.now()} }
        newvaluesForDunke = { "$set": { 'dunke': datetime.datetime.now()} }
        collection.update_one(filterBolde,newvaluesForBolde)
        collection.update_one(filterDunke,newvaluesForDunke)
        print(request.form["bolde"])
        return render_template('index.html',listofitems=collection.find())
    
    return render_template('index.html',listofitems=collection.find())


if __name__ == "__main__":
    app.run(debug=True, port=8080)