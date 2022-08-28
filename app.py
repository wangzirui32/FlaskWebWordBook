from flask import Flask
from flask import render_template, request
from tinydb import TinyDB, Query
from utils import get_word_data

app = Flask(__name__)
db = TinyDB("db.json")
words_table = db.table("words")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/show/<word>")
def show(word):
    return render_template("show.html", word=word)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/api/word", methods=["GET", "POST", "DELETE"])
def api_word():
    if request.method == "GET":
        words = words_table.all()
        return {"data": words} if words else {"data": []}
    elif request.method == "POST":
        word = request.form.get("word")
        if not words_table.contains(Query().word == word):
            words_table.insert({"word": word})
        return {"code": 200}    
    elif request.method == "DELETE":
        word = request.form.get("word")
        words_table.remove(Query().word == word)
        return {"code": 204}, 204

@app.route("/api/get-word-data")
def api_get_word_data():
    word = request.args.get("word")
    return get_word_data(word)

if __name__ == "__main__":
    app.run(debug=True)