from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return {"data": "Hello Flask!"}

@app.route('/current_datetime',methods=['GET'])
def current_datetime():
    timer = datetime.now()
    timerJob = timer.strftime('%H')
    msg =""
    curr_datetime= timer.strftime("%d/%m/%Y %H:%M:%S %p")
    if int(timerJob[0]) == 0 : msg = "Bom dia!"
    elif int(timerJob) > 11:
        if int(timerJob) < 18 : msg = "Boa tarde!" 
        else : msg = "Boa noite!" 
    send ={"current_datetime": curr_datetime, "message": msg}
    return send
