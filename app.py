from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import os
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	link = 'https://finnhub.io/api/v1/stock/profile2?symbol='
	rest = '&token=bvgkhuv48v6oab530qmg'
	r = requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=bvgkhuv48v6oab530qmg')
	stuff = r.json()
	print(len(stuff))
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run()
