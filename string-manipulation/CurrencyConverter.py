class CurrencyConverter:
    currency = {
        'dolar': {
            'symbol': '$',
            'price': {
                'dolar': 1,
                'euro': 0.82,
                'real': 5.2
            }
        },
        'real': {
            'symbol': 'R$',
            'price': {
                'dolar': 0.19,
                'euro': 0.16,
                'real': 1
            }
        },
        'euro': {
            'symbol': '€',
            'price': {
                'dolar': 1.22,
                'euro': 1,
                'real': 6.37
            }
        }
    }

    def __init__(self, origin, target, quantity):
        self.origin = origin
        self.target = target
        self.quantity = quantity

    def convert(self):
        currency = getattr(self, 'currency')
        return currency[self.origin]["price"][self.target] * self.quantity

    def __str__(self):
        currency = getattr(self, 'currency')
        return f'Origin: {self.origin}\n' \
               f'Target: {self.target}\n' \
               f'Quantity: {self.quantity}\n' \
               f'{currency[self.origin]["symbol"]}{"{:.2f}".format(self.quantity)} is ' \
               f'{currency[self.target]["symbol"]}{"{:.2f}".format(self.convert())}'
