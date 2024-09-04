# Polimorfismo é basicamente uma mesma função que se comporta de maneiras diferentes para tipos diferentes
# len() é um exemplo de polimorfismo:

# len("String") == conta os caracteres
len("String") #6

# len([1, 2, 3]) == conta os elementos da lista
len([1, 2, 3]) #3

# Polimorfismo com Herança

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("O Avestruz não pode voar")


def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

print("teste pardal:")
plano_voo(p1)

print("teste avestruz")
plano_voo(p2)