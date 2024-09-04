# O conceito de herança é literalmente subclasses que herdam caracteristicas da constructor da classe pai

class Veiculo:
    def __init__(self, cor, placa, qtd_rodas):
        self.cor = cor
        self.placa = placa
        self.qtd_rodas = qtd_rodas

    def ligar_motor(self):
        print("Ligando Motor")


# Sintaxe para herdar class Filha(Pai)
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    # Esse init SOBRESCREVE o init da classe Pai
    def __init__(self, cor, placa, qtd_rodas, estepe):
        self.estepe = estepe

    def possui_step(self):
        print(f"{'Sim' if self.estepe else 'Não'} possui estepe")

class Caminhao(Veiculo):
    # Ao usar super, esse init COMPLEMENTA o init da classe pai
    def __init__(self, cor, placa, qtd_rodas, carregado):
        super().__init__(cor, placa, qtd_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim'  if self.carregado else 'Não'} estou carregado!")


moto = Motocicleta("Preta", "abc-1234", 2)
print("="*30)
print("Testando Herança na moto (Função Vazia)")
moto.ligar_motor()

print("="*30)
print("Testando Herança no carro (__init__ sobrescrevendo)")
carro = Carro("Verde", "tse-1234", 4, False)
carro.ligar_motor()
carro.possui_step()

print("="*30)
print("Testando Herança no caminhão (__init__ complementando)")
caminhao = Caminhao("Vermelho", "dsa-2112", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

