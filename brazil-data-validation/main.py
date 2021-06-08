from register import Register

document = input('Digite o numero do documento: ')
phone = input('Digite o numero do telefone: ')
cep = input('Digite o numero do cep: ')
register = Register(document, phone, cep)


print(register)