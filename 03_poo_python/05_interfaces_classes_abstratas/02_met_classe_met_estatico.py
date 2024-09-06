# METODOS DE INSTANCIA: Visto anteriormente, referenciam instancias (self)

# METODOS DE CLASSE (classmethod): referenciam a classe (cls)

# METODOS ESTÁTICOS: não dependem nem de "cls" e nem de "self" são como funções normais que são agrupada dentro da classe por questões de organização

class Pessoa:
    def __init__(self, nome, idade):
        # o valor de "self" é "p"
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        # o valor de "cls" é "Pessoa"
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

