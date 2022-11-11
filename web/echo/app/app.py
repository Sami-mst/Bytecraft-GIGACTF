#!/usr/bin/python3
from flask import Flask, Response, request, render_template, make_response
import os
import subprocess

app = Flask(__name__)


@app.route("/",methods = ["GET"])
def main():
    return render_template('index.html')

@app.route("/",methods = ["POST"])
def main2():
    cmd = request.values.get('input')
    cmd = f'echo {cmd}'
    return subprocess.check_output(cmd, shell=True).decode('ascii')
