
""" MODELANDO O SISTEMA BANCÁRIO

OBJETIVO
  -> Armazenar dados de clientes e contas bancárias em objetos ao invés de dicionários
  -> Adicionar classes para CLIENTE e para as operações de DEPÓSITO e SAQUE.
  -> Seguir o modelo de UML disponibilizado

"""
import datetime
from abc import ABC, abstractmethod

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor  

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def agencia(self):
        return self._agencia
  
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        print("===== SAQUE =====")
        saldo = self.saldo

        if valor > saldo:
            print("Falha! Saldo Insuficiente. ")
        
        elif valor > 0: 
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

            return True

        else:
            print("Falha! valor inválido.")
        
        return False

    def depositar(self, valor):  
        print("===== DEPÓSITO =====")
        
        if  valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        
        else:
            print("Falha! valor inválido.")

        return True

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite=500, limite_saques=3):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self.limite:
            print(f"Falha! Excedeu limite de R$ {self.limite:.2f} por saque.")

        elif numero_saques >= self.limite_saques:
            print(f"Falha! Excedeu o limite de {self.limite_saques} saques diários.")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s",)
            }
        )

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

def menu():
    print("""
    =========== MENU ==========

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nu] Novo Usuário
        [lu] Listar Usuários
        [nc] Nova Conta
        [lc] Listar Contas

        [q] Sair

    ===========================
    => """)
    
def main():
        
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = "OPERAÇÃO     VALOR\n"
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = input(menu).lower()

        if opcao == "d":
            deposito = float(input("Insira o valor de DEPOSITO => R$ "))
            saldo, extrato = depositar(deposito, saldo, extrato)


        elif opcao == "s":
            saque = float(input("Insira o valor de SAQUE => R$ "))
            saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    saque=saque,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            apresentar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida, por favor selecione uma opção válida")

main()

        