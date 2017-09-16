from flask import Flask, render_template, request, jsonify
from random import randint
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/analyzer')
def startAnalyzer():
    return render_template('start.html');

@app.route("/result", methods=["GET", "POST"])
def getResponses():
    if request.method == "POST":
        data = {}
        responseData = {}
        data = request.form
        if data["type"] != "hello_msg" and data["type"] != "name_input" and data["type"] != "welcome":
            responseData["level"] = randint(1, 5)
        else:
            responseData["level"] = 0
        responseData["question"] = data["question"]
        responseData["type"] = data["type"]
        return jsonify(responseData)

if __name__ == '__main__':
   app.run(debug = True)
