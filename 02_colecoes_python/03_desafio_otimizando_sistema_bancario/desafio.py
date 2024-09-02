
""" APRIMORANDO O SISTEMA BANCÁRIO

OBJETIVO
  -> Separar as funcionalidades existentes em funções de Saque, Deposito e Extrato
  -> Criar duas novas funções: Cadastrar usuário; Cadastrar conta bancária

FUNÇÃO DEPOSITO 
  -> Deve receber apenas argumentos posicionais (positional only)

FUNÇÃO SAQUE 
  -> Deve receber apenas argumentos por nome (keyword only)

FUNÇÃO EXTRATO 
  -> Deve receber argumentos por posição e nome
  -> Argumentos posicionais: saldo
  -> Argumentos nomeados: extrato

CRIAR USUÁRIO
  -> Devem ser armazenados em lista
  -> Propriedades: nome, data de nascimento, cpf e endereço
  -> Endereço é uma string com: logradouro - bairro - cidade/sigla estado
  -> CPF: Somente números e único

CRIAR CONTA 
  -> Devem ser armazenados em lista
  -> Propriedades: agência, número da conta e usuário
  -> O número da conta é fixo ("0001")
  -> Um usuário pode ter muitas contas, mas uma conta só pertence a um usuário


"""
menu = """
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
=> """

def depositar(deposito, saldo, extrato, /):
    print("===== DEPÓSITO =====")
    
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito   R$ {deposito:.2f} \n"
        print(f" R$ {deposito:.2f} Depositados com sucesso!")
    else:
        print("Valor de depósito inválido!")

    return saldo, extrato


def sacar(*, saque, saldo, extrato, numero_saques, limite, limite_saques):
    print("===== SAQUE =====")
    
    if saque > saldo:
        print("Erro! Saldo insuficiente!")

    elif saque > limite:
        print("Erro! Máximo R$ 500.00 por saque")

    elif numero_saques >= limite_saques:
        print("Erro! Limite de 3 saques diários atingido")

    elif saque > 0:
        saldo -= saque
        extrato += f"Saque      R$ {saque:.2f} \n"
        numero_saques += 1
        print(f" R$ {saque:.2f} Sacados com sucesso!")
        print(f"n de saque = {numero_saques}")

    else:
        print("Valor de saque inválido!")
    
    return saldo, extrato, numero_saques


def apresentar_extrato(saldo, /, *, extrato):
    print("========== EXTRATO ==========")
    print(extrato)
    print(f"SALDO ATUAL: R$ {saldo:.2f}")
    print("=============================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_usuarios(usuarios):
    print("===== USUÁRIOS CADASTRADOS =====")
    print("CPF\t\tNome\t\t\t\tData Nascimento")
    for usuario in usuarios:
        print(f"\n{usuario["cpf"]}\t\t{usuario["nome"]}\t\t\t{usuario["data_nascimento"]}")
    print("=" * 100)   
    


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


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

        