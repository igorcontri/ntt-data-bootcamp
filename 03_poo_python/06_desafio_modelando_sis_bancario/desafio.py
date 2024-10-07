
""" MODELANDO O SISTEMA BANCÁRIO

OBJETIVO
  -> Armazenar dados de clientes e contas bancárias em objetos ao invés de dicionários
  -> Adicionar classes para CLIENTE e para as operações de DEPÓSITO e SAQUE.
  -> Seguir o modelo de UML disponibilizado

"""
import textwrap
from datetime import datetime
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
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self._limite:
            print(f"Falha! Excedeu limite de R$ {self._limite:.2f} por saque.")

        elif numero_saques >= self._limite_saques:
            print(f"Falha! Excedeu o limite de {self._limite_saques} saques diários.")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente._nome}
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
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
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


def depositar(clientes):
    print("===== DEPÓSITO =====")
    
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("CPF não encontrado!")
        return
    
    valor = float(input("Valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    print("===== SAQUE =====")
    
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("CPF não encontrado!")
        return
    
    valor = float(input("Valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
# Possibilidade de unir Depósito e Saque em uma só função (transacao)

def recuperar_conta_cliente(cliente):
    if not cliente._contas:
        print("Esse cliente não possui conta.")
        return
    
    # Retorna a primeira conta do cliente, mas poderia criar uma opção de escolha para o cliente
    # A opção de escolha gera um pouco mais de complexidade
    return cliente._contas[0]


def apresentar_extrato(clientes):
    print("===== EXTRATO =====")
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("CPF não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("========== EXTRATO ==========")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Sem movimentações registradas."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\t R$ {conta.saldo:.2f}")
    print("=============================")


def cadastrar_cliente(clientes):
    print(" ==== CADASTRANDO CLIENTE ====")
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nJá existe um cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("=== Usuário criado com sucesso! ===")


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("CPF não encontrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente._contas.append(conta)

    print(" === Conta Criada com Sucesso! ===")


def listar_usuarios(usuarios):
    print("===== USUÁRIOS CADASTRADOS =====")
    print("CPF\t\tNome\t\t\t\tData Nascimento")
    for usuario in usuarios:
        print(f"\n{usuario["cpf"]}\t\t{usuario["nome"]}\t\t\t{usuario["data_nascimento"]}")
    print("=" * 100)   
    

def listar_contas(contas):
    for conta in contas:
        print("="*100)
        print(textwrap.dedent(str(conta)))


def menu():
    opcao = input("""
    =========== MENU ==========

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas

        [q] Sair

    ===========================
    => """).lower()

    return opcao


def main():

    clientes = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            apresentar_extrato(clientes)

        elif opcao == "nu":
            cadastrar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida, por favor selecione uma opção válida")

main()

        