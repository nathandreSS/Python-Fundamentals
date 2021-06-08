import re


class Phone:
    pattern = '([0-9]{2})([0-9]{5})([0-9]{4})'
    pattern = '([0-9]{2})([0-9]{5})([0-9]{4})'

    def __init__(self, number):
        if self.validate(number):
            self.number = number
        else:
            raise ValueError('Invalid phone number!')

    @staticmethod
    def validate(number):
        return re.search(Phone.pattern, number)

    def format(self):
        number = re.search(Phone.pattern, self.number)
        ddd = number.group(1)
        before_hyphen = number.group(2)
        after_hyphen = number.group(3)
        return f'Telefone: (+55)({ddd}){before_hyphen}-{after_hyphen}'

    def __str__(self):
        return self.format()