class APIHandler:
    def __init__(self, currency_converter):
        self.currency_converter = currency_converter

    def get_currency_rate(self, currency_code):
        if currency_code not in self.currency_converter.currency_rates:
            raise ValueError("Currency not found")

        return self.currency_converter.currency_rates[currency_code]


