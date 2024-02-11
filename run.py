import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/log_in")
def log_in():
    return render_template("log_in.html")



if  __name__ == "__main__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True
              )