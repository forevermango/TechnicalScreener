from flask import Flask, render_template
from patterns import patterns
import yfinance as yf
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', patterns=patterns)

@app.route('/snapshot')
def snapshot():
    with open('datasets/companies.csv') as f:
        symbols = f.read().splitlines()
        print(symbols)

    return {
        'code': 'success'
    }