from crypt import methods
import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'page'


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/result', methods=['post'])
def result():
    # print(request.form["name"])
    # print(request.form["location"])
    # print(request.form["lenguaje"])
    # print(request.form["comments"])
    session['form'] = request.form

    return redirect("/response")


@app.route('/response')
def response():
    print(session['form']["name"])
    print(session['form']["location"])
    print(session['form']["lenguaje"])
    print(session['form']["comments"])

    return render_template("response.html")


if __name__ == "__main__":
    app.run(debug=True)
