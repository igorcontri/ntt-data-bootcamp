
""" MODELANDO O SISTEMA BANCÁRIO

OBJETIVO
  -> Armazenar dados de clientes e contas bancárias em objetos ao invés de dicionários
  -> Adicionar classes para CLIENTE e para as operações de DEPÓSITO e SAQUE.
  -> Seguir o modelo de UML disponibilizado

"""
from abc import ABC, abstractmethod

class Transacao(ABC):

    @abstractmethod
    def registrar(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor    

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
        
        # if saque > saldo:
        #     print("Erro! Saldo insuficiente!")

        # elif saque > limite:
        #     print("Erro! Máximo R$ 500.00 por saque")

        # elif numero_saques >= limite_saques:
        #     print("Erro! Limite de 3 saques diários atingido")

        # elif saque > 0:
        #     saldo -= saque
        #     extrato += f"Saque      R$ {saque:.2f} \n"
        #     numero_saques += 1
        #     print(f" R$ {saque:.2f} Sacados com sucesso!")
        #     print(f"n de saque = {numero_saques}")

    def depositar(self, valor):  
        print("===== DEPÓSITO =====")

        # if deposito > 0:
        #     saldo += deposito
        #     extrato += f"Depósito   R$ {deposito:.2f} \n"
        #     print(f" R$ {deposito:.2f} Depositados com sucesso!")
        # else:
        #     print("Valor de depósito inválido!")

        # return saldo, extrato


class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques

class Historico:
    def adicionar_transacao():
        pass

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

        