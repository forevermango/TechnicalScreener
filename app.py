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
        companies = f.read().splitlines()
        for company in companies: 
            symbol = company.split(',')[0]
            df = yf.download(symbol, start="2020-01-01", end="2020-12-16")
            df.to_csv('datasets/daily/{}.csv'.format(symbol))

    return {
        'code': 'success'
    }