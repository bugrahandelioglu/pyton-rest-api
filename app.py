from flask import Flask, request, redirect, jsonify
from datetime import datetime
import requests
import json

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

@app.route('/post_notify', methods=["GET", "POST"])
def post_ex():
    if request.method == "POST":
        body = request.json
        print(f'\n{body}\n')

    return jsonify({"uuid":"test"})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
