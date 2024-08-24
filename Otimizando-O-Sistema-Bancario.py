import textwrap

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R${valor:.2f}\n"
        print("Depósito Efetuado com Sucesso!")
    else:
        print("Operação falhou! O valor é inválido")
    return saldo, extrato

def sacar(valor, saldo, extrato, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor <= saldo:
            saldo -= valor
            extrato += f"Retirada de R${valor:.2f}\n"
            numero_saques += 1
            print("Saque Efetuado com Sucesso!")
        else:
            print("Operação falhou! O valor do saque excede o limite.")
    else:
        print("Operação falhou! Número máximo de saques excedido")
    return saldo, extrato, numero_saques

def menu():
    print("""\n
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Usuário
    [5] Nova Conta
    [6] Lista de Contas
    [0] sair
    =>""")
    return input().strip()

def criar_usuario(usuarios):
    cpf = input("Informe o CPF:(Somente Número) ")
    if filtrar_usuario(cpf, usuarios):
        print(f"Já existe usuário com esse CPF {cpf}")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (Logradura, Número, Cidade, Estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado, Operação cancelada.")
        print("Não tem como criar uma conta sem usuário.")
        print("Digite '4' para criar um usuário.")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    saldo = 0
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: R$ "))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: R$ "))
            saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, limite_saques)

        elif opcao == "3":
            print("===== Extrato =====\n")
            print(extrato)
            print(f"Saldo na Conta R${saldo:.2f}")

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Programa Finalizado.")
            break

        else:
            print("Operação inválida, Selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
