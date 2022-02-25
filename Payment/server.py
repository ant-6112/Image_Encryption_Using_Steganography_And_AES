import json
import os
import stripe
from flask import Flask, render_template, jsonify
from flask import key,request
import try

key.stripe.api_key = "sk_test_51GrPHpIZCvIu1oR1cBOrFofm3CJMmUFpzAk8g2PX8weKjfy2Q5ezAifwa2UxrTiCxKNkfVJwhVcF6ntJKuOCzS8000Iz6Ykbi5"

request
app = Flask(__name__, static_folder = ".",static_url_path = "", template_folder = ".")

def calculate_order_amount(items): 
        return 1400@app.route('/create-payment-intent', methods = ['POST'])

def create_payment():
	try :
	    data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(amount = calculate_order_amount(data['items']),currency = 'usd')
		#return jsonify({'clientSecret': intent['client_secret']})
	except Exception as e:
		return jsonify(error = str(e)), 403

if __name__ == '__main__':
	app.run()