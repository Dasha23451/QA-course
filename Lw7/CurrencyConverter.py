class CurrencyConverter:
    def __init__(self, currency_rates):
        self.currency_rates = currency_rates

    def convert_currency(self, from_currency, to_currency, amount):
        if from_currency not in self.currency_rates or to_currency not in self.currency_rates:
            raise ValueError("Currency not found")

        from_rate = self.currency_rates[from_currency]
        to_rate = self.currency_rates[to_currency]
        converted_amount = amount * (to_rate / from_rate)

        return converted_amount
