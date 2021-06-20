# save this as app.py
from flask import Flask, render_template,request, jsonify
import sys 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', name='temp')
@app.route("/submit", methods=['POST'])
def submit():
    inout=request.values['inout']
    date=request.values['date']
    type=request.values['type']
    money=request.values['money']
    descript=request.values['descript']
    return render_template('submit.html',**locals())
if __name__ == '__main__':
    app.run(debug = True)
   