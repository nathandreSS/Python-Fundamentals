from datetime import datetime, timedelta
from document import Document
from phone import Phone
from address import Address


class Date:
    months = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]

    def __init__(self, date):
        if type(date) == datetime:
            self.date = date
        else:
            raise ValueError('Date is not a datetime instance!')

    def __str__(self):
        day = self.date.day
        month = Date.months[self.date.month - 1]
        year = self.date.year
        return f'Criado no dia {day} de {month} de {year}'

    def __sub__(self, other):
        return other - self.date


class Register:
    def __init__(self, document, phone, cep):
        self.document = Document.create(document)
        self.phone = Phone(phone)
        self.address = Address(cep)
        self.created_at = Date(datetime.now())

    def time(self):
        return datetime.now() - self.created_at.date

    def __str__(self):
        return f'{self.document}\n' \
               f'{self.phone}\n' \
               f'{self.address}\n' \
               f'{self.created_at}'