import os
from flask import Flask, render_template, url_for, request,  redirect
if os.path.exists("env.py"):
    import env
from flask_pymongo import PyMongo

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/log_in")
def log_in():
    return render_template("log_in.html")



@app.route("/register")
def  register():
    return render_template("register.html")



if  __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
              )

