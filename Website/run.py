from flask import Flask, render_template, request, jsonify
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
        data = request.form

        print(data)

        return jsonify(data)

if __name__ == '__main__':
   app.run(debug = True)
