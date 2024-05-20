from flask import Flask, jsonify, request
from CurrencyConverter import CurrencyConverter
from APIHandler import APIHandler
app = Flask(__name__)

currency_rates = {
    "USD": 90.98,
    "EUR": 98.78,
    "GBP": 115.26,
    "JPY": 0.58,
    "AUD": 60.71,
    "CAD": 66.80,
    "CHF": 100.0,
    "CNY": 12.57,
    "RUB": 1.0,
    "KRW": 0.067,
    "BRL": 17.74,
    "BYN": 28.28,
}

currency_converter = CurrencyConverter(currency_rates)
api_handler = APIHandler(currency_converter)

@app.route('/currencies', methods=['GET'])
def get_currencies():
    return jsonify(currency_rates)


@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount', 1.0))

    converted_amount = currency_converter.convert_currency(from_currency, to_currency, amount)

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted_amount": converted_amount
    })


if __name__ == '__main__':
    app.run(debug=True)
