from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def say_welcome():
    ''' Return simple "welcome" '''
    html = "<html><body><h2>welcome</h2></body></html>"
    return html

@app.route('/welcome/back')
def say_wb():
    ''' return a welcome back '''
    html = "<html><body><h2>welcome back</h2></body></html>"
    return html


@app.route('/welcome/home')
def say_welcome_home():
    ''' return a welcome home '''
    html = "<html><body><h2>welcome home</h2></body></html>"
    return html
