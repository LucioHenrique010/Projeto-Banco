from datetime import datetime

ano_vigente = datetime.today().year # -> Extrai o ano vigente

class PessoaFisica:
    def __init__(self, nome:str, genero:str, nascimento:int, cpf:str):
        
        self._nome = None
        self.nome = nome

        self._genero = None
        self.genero = genero

        self._nascimento = None
        self.nascimento = nascimento
        
        self._cpf = None
        self.cpf = cpf

        
    # GETTER do nome
    @property
    def nome(self):
        return self._nome
    # SETTER do nome, aqui é avaliado se um nome é válido.
    @nome.setter
    def nome(self, valor:str):
        if valor.strip().isalpha():
            self._nome = valor.strip().capitalize()
        else:
            raise ValueError("Nome inválido!")


    # GETTER do CPF
    @property
    def cpf(self):
        return self._cpf
    # SETTER do CPF, aqui é avaliado se um CPF é válido.
    @cpf.setter
    def cpf(self, valor:str):
        if len(valor.strip()) == 6 and valor.isnumeric():
            self._cpf = valor
        else:
            raise ValueError("CPF inválido!")


    # GETTER do gênero
    @property
    def genero(self):
        return self._genero
    # SETTER do gênero, aqui é avaliado se um gênero é válido.
    @genero.setter
    def genero(self, valor:str):
        if valor.strip().upper()[0] == "M":
            self._genero = "M"
        elif valor.strip().upper()[0] == "F":
            self._genero = "F"
        else:
            raise ValueError("Gênero inválido!")


    # GETTER do ano de nascimento
    @property
    def nascimento(self):
        return self._nascimento
    # SETTER do ano de nascimento, aqui é avaliado se o ano de nascimento é válido.
    @nascimento.setter
    def nascimento(self, valor:int):
        if valor <= ano_vigente and valor >= 1900:
            self._nascimento = valor
        else:
            raise ValueError("Ano de nascimento inválido!")
    # GETTER da idade
    @property
    def idade(self):
        return (ano_vigente - self._nascimento)
