from flask import Flask, render_template,redirect,request,url_for
from config import config
app= Flask(__name__)
@app.route("/")

def index():
    return redirect("login")

@app.route("/login")
def login():
    return render_template("auth/login.html")


if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.run()