from __future__ import print_function
from flask import Flask, render_template, request, jsonify, send_file
from random import randint
import multiclass
import sys
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/analyzer')
def startAnalyzer():
    return render_template('start.html');

@app.route('/postchart', methods=["GET", "POST"])
def postChart():
    if request.method == "POST":
        global chartData
        chartData = request.form
        print(chartData, file=sys.stdout)
    return jsonify(chartData)

@app.route('/getchart', methods=["POST", "GET"])
def getChart():
    if request.method == "GET":
        return jsonify(chartData)


@app.route('/chart', methods=["GET", "POST"])
def chart():
    return render_template('chart.html')

@app.route("/result", methods=["GET", "POST"])
def getResponses():
    if request.method == "POST":
        data = {}
        responseData = {}
        data = request.form
        responseData["level"] = multiclass.process(data["answer"])
        responseData["question"] = data["question"]
        responseData["type"] = data["type"]
        return jsonify(responseData)

@app.route("/getquestions", methods=["GET", "POST"])
def getQuestions():
    if request.method == "GET":
        return send_file('questions.csv',
                     mimetype='text/csv',
                     attachment_filename='questions.csv',
                     as_attachment=True)
    return result

if __name__ == '__main__':
   app.run(debug = True)
