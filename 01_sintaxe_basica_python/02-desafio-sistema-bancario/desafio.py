
""" CRIANDO UM SISTEMA BANCÁRIO COM PYTHON

REGRAS 

DEPOSITO 
  -> Não depositar valores negativos
  -> Todos os depositos devem ser armazenados em uma variável e exibidos em uma operação de extrato

SAQUE 
  -> Máximo 3 saques diários, 
  -> Máximo R$ 500,00 por saque
  -> Informar o usuário em caso de saldo insuficiente (saque > saldo)
  -> Todos os saques devem ser armazenados em uma variável e exibidos em uma operação de extrato

EXTRATO 
  -> Listar todos os depositos e saques realizados na conta
  -> Apresentar saldo atual no fim da listagem
  -> Os valores devem ser exibidos no formato R$ XXXX.XX (R$ 1500.00)
"""

menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = "OPERAÇÃO     VALOR\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        print("--- DEPÓSITO ---")
        deposito = float(input("Insira o valor de DEPOSITO => R$ "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito   R$ {deposito:.2f} \n"
            print(f" R$ {deposito:.2f} Depositados com sucesso!")
        else:
            print("Valor de depósito inválido!")


    elif opcao == "s":
        print("--- SAQUE ---")
        
        saque = float(input("Insira o valor de SAQUE => R$ "))

        if saque > saldo:
            print("Erro! Saldo insuficiente!")
        elif saque > 500:
            print("Erro! Máximo R$ 500.00 por saque")
        elif numero_saques >= LIMITE_SAQUES:
            print("Erro! Limite de 3 saques diários atingido")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque      R$ {saque:.2f} \n"
            numero_saques += 1
            print(f" R$ {saque:.2f} Sacados com sucesso!")
        else:
            print("Valor de saque inválido!")
    
    elif opcao == "e":
        print("--- EXTRATO ---")
        print(extrato)
        print(f"SALDO ATUAL: R$ {saldo:.2f}")
        print("---------------")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione uma opção válida")

    