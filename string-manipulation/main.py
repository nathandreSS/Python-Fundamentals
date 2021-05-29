from ExtractorURL import ExtractorURL
from CurrencyConverter import CurrencyConverter

#"bytebank.com/cambio?quantity=100&origin=real&target=euro"
url = input('Informe a URL: ')

extractor_url = ExtractorURL(url)

origin = extractor_url.params['origin']
target = extractor_url.params['target']
quantity = float(extractor_url.params['quantity'])

currency_converter = CurrencyConverter(origin, target, quantity)

print(currency_converter)
