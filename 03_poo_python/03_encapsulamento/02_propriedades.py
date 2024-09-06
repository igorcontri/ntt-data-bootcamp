class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024  
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Igor", 1998)
print(f"Nome: {pessoa.nome}\tIdade: {pessoa.idade}")


# BREVE RESUMO SOBRE DECORATORS
# Decorators recebem a função abaixo do "@" como argumento, ou seja:

# @property
# def nome(self):

# É o mesmo que:

# def property(func):
#   lógica...

# property(nome)