from flask import abort, Flask, jsonify, request
import requests
import json
import os

app = Flask(__name__)

@app.route("/")
def PostHumid():
    ACCESS_URL = ""
    SLACK_URL = ""
    temp = ""
    humid = ""
    abs_humid = ""
    message = ""

    ACCESS_URL = os.environ["ACCESS_URL"]
    SLACK_URL = os.environ["SLACK_URL"]
    temp = request.args.get('temp')
    humid = request.args.get('humid')
    abs_humid = request.args.get('abs_humid')

    if temp == "" or humid == "" or abs_humid == "":
        message = "センサーエラーです"
    elif float(abs_humid) > 15: 
        message = "部屋の湿度が高いです\n絶対湿度は" + abs_humid + "です"
    elif float(abs_humid) < 5:
        message = "部屋が乾燥しています\n絶対湿度は" + abs_humid + "です"

    flug = requests.get(ACCESS_URL+"get")

    if flug.text == "0" and message != "":
        requests.post(SLACK_URL,data=json.dumps({
            "text" : message
        }))

    return "hello"
