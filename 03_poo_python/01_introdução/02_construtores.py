# O método construtor sempre é executado quando uma nova instância da classe é criada

# __init__ é responsável por declarar qual é o método construtor da classe
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print(f"{self.nome} diz: au")

c = Cachorro("Toddy", "Preto")
c.latir()


# Métodos destrutores (nao muito utilizado em python) é executado quando uma instância é destruida.
# __del__ é responsável por declarar qual é o método destrutor da classe

class Rato:
    def __del__(self):
        print("Destruindo Instância do rato")

r = Rato()
del r