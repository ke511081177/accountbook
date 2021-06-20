# save this as app.py
from flask import Flask, render_template,request, jsonify
import pygsheets
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
    who=request.values['who']
    gc = pygsheets.authorize(service_file='authentic-ether-317408-d4d7f9c28d92.json')
    sht = gc.open_by_url(
    'https://docs.google.com/spreadsheets/d/1FBUrlvbCjp0Ae4mE3OccniPPgHHg98vGhxSQILJNgxM/'
    )
    wks_list = sht.worksheets()
    print(wks_list)
    #選取by順序
    wks = sht[0]
    print(wks)
    #選取by名稱
    #wks = sht.worksheet_by_title("202106")

    #更新名稱
    output=[ date,who,inout,type,money,descript]
    wks.append_table(values=output)

    #隱藏清單
    #wks.hidden = False
    #wks.update_cell('A2:A5',"Hey yank this numpy array")
    return render_template('submit.html',**locals())


if __name__ == '__main__':
    #app.run(debug = True)
    app.run(host="0.0.0.0", port=8090)
