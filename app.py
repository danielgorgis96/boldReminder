from flask import Flask, render_template
app = Flask(__name__)
import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:2LlSMHZHg6axsock@cluster0.2vhzr6w.mongodb.net/?retryWrites=true&w=majority")
db = client["db"]
collection = db.get_collection("users")

for item in collection.find():
    print(item)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)