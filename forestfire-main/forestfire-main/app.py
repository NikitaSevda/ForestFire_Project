from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

app.route('/')
def home():
    pass

if __name__=="__main__":
    app.run(host="0.0.0.0")
