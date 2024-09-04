# Recursos são divididos em Públicos e Privados
# Em algumas linguagens há palavras reservadas para definir estes recursos, porém em python há uma convenção 

# Publico -> Pode ser acessado de fora da classe.
# Privado -> Só pode ser acessado pela classe. (Estes são representados em python iniciando com um "underline")

class Conta:
    def __init__(self, n_agencia, saldo=0):
        # exemplo de recurso PRIVADO
        self._saldo = saldo
        # exemplo de recurso PUBLICO
        self.n_agencia = n_agencia

    def depositar(self, valor):
        # O método depoisitar é acessado FORA da classe, porém o "_saldo" é tratado apenas dentro da classe
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
conta = Conta(100)



# === USO DO RECURSO PRIVADO ====
# A ideia é que NÃO FAÇA o acesso a essa variável dessa forma (fora da classe), pois _saldo foi definido como PRIVADO 

# conta._saldo += 100
# print(conta._saldo)

# Maneira correta, sempre ter um método para acessar a variável privada
conta.depositar(100)

# === USO DO RECURSO PUBLICO ===
# Nessa situação, não há problemas acessar "n_agencia" fora da classe, pois NÃO foi definido como privado
print(conta.n_agencia)
print(conta.mostrar_saldo())