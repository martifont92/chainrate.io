from flask import Blueprint, render_template, url_for

main = Blueprint('main',__name__)

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/exchanges')
def exchanges():
	return render_template('exchanges.html')

@main.route('/wallets')
def wallets():
	return render_template('wallets.html')

@main.route('/cards')
def cards():
	return render_template('cards.html')

@main.route('/whereToBuy')
def whereToBuy():
	return render_template('whereToBuy.html')