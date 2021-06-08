from validate_docbr import CPF, CNPJ


class Document:

    @staticmethod
    def create(document):
        document = str(document)
        if len(document) == 11:
            return MyCPFClass(document)
        elif len(document) == 14:
            return MyCNPJClass(document)
        else:
            raise ValueError("Invalid number of digits!")


class MyCPFClass:

    def __init__(self, document):
        if self.validate(document):
            self.cpf = document
        else:
            raise Exception('Invalid CPF!')

    @staticmethod
    def validate(document):
        cpf = CPF()
        return cpf.validate(cpf.mask(document))

    def format(self):
        cpf = CPF()
        return cpf.mask(self.cpf)

    def __str__(self):
        return f'CPF: {self.format()}'


class MyCNPJClass:

    def __init__(self, document):
        if self.validate(document):
            self.cnpj = document
        else:
            raise Exception('Invalid CNPJ!')

    @staticmethod
    def validate(document):
        cnpj = CNPJ()
        return cnpj.validate(cnpj.mask(document))

    def format(self):
        cnpj = CNPJ()
        return cnpj.mask(self.cnpj)

    def __str__(self):
        return f'CNPJ: {self.format()}'
