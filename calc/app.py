from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def result_add():
    ''' add the result to body'''
    val1 = int(request.args["a"])
    val2 = int(request.args["b"])
    result = add( val1, val2)
    html = f"<html><body><h2>{result}</h2></body></html>"
    return html

    
