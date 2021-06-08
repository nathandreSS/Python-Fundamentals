import re
import requests


class CEP:
    pattern = '([0-9]{5})([0-9]{3})'

    def __init__(self, cep):
        cep = str(cep)
        self.validate(cep)
        self.cep = cep

    @staticmethod
    def validate(cep):
        if len(cep) != 8:
            raise ValueError("CEP Invalido!")

    def format(self):
        cep = re.search(CEP.pattern, self.cep)
        return f'{cep.group(1)}-{cep.group(2)}'

    def __str__(self):
        return self.format()


class Address:
    def __init__(self, cep):
        cep = str(cep)
        self.cep = CEP(cep)
        self.state, \
            self.city, \
            self.district, \
            self.street = self.search_address()

    def search_address(self):
        response = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        data = response.json()
        return data['uf'], data['localidade'], data['bairro'], data['logradouro']

    def __str__(self):
        return f'CEP: {self.cep}\n' \
               f'Estado: {self.state}\n' \
               f'Cidade: {self.city}\n' \
               f'Bairro: {self.district}\n' \
               f'Logradouro: {self.street}\n'
