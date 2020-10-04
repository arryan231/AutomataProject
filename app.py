from flask import Flask, render_template, request
import jsonify
import requests
app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@app.route("/convert", methods=['POST'])
def convert():
    pass
if __name__=="__main__":
    app.run(debug=True)
