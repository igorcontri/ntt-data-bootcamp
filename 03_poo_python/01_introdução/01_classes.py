class Bruxo:
    # construtor
    def __init__(self, nome, escola, idade, contratos):
        self.nome = nome
        self.escola = escola
        self.idade = idade
        self.contratos = contratos

    # metodo são funções dentro de uma classe
    # metodo 1
    def atacar(self):
        print(f"{self.nome} ataca com espada!")

    # metodo 2
    def ign(self):
        print(f"{self.nome} conjura chamas com sinal Ign!")

    # metodo 3
    def quen(self):
        print(f"{self.nome} se defende com o sinal Quen!")

print("========= BRUXO 1 ========")
bruxo_1 = Bruxo("Geralt", "Lobo", "104", 5000)
print(bruxo_1.nome, bruxo_1.escola, bruxo_1.idade, bruxo_1.contratos)
bruxo_1.atacar()
bruxo_1.ign()
bruxo_1.quen()

print("========= BRUXO 2 ========")
bruxo_2 = Bruxo("Vesemir", "Lobo", "300", 10000)
Bruxo.atacar(bruxo_2) #bruxo_2.atacar()