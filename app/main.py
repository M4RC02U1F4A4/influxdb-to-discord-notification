from flask import Flask, request
import requests
import os
import json

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def home():
    data = json.loads(request.data.decode())
    r = requests.post(f"{os.getenv('LINK')}", json={"content":f"{data['_message']}"})
    return "OK", 200