import textwrap

def depositar (valor):
    global saldo
    global extrato
    if valor > 0: 
        saldo += valor
        extrato += ("Depósito de R${:.2f}\n".format(valor))
        print("Depósito Efetuado com Sucesso!")
    else:
        print("Operação falhou! O valor é inválido")
    return saldo, extrato

def sacar (valor):
    global numero_saques
    global limite_saques
    global saldo
    global extrato
    if numero_saques < limite_saques:
        if valor <= saldo:
            saldo -= valor
            extrato += ("Retirada de R${:.2f}\n".format(valor))
            numero_saques += 1
        else:
            print("Operação falhou! O valor do saque excede o limite.")
    else:
        print("Operação falhou! Número máximo de saques excedido")
    return saldo, extrato

def menu():
    print("""\n
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Lista de Contas
    [6] Novo Usuário
    [0] sair
    =>""")
    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF:(Somente Número)")
    usuaria = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("Já existe usúario com esse CPF{}".format(cpf))
        return

    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento:(dd/mm/aaaa)")
    endereco = input("Informe o endereço (Logradura,Número,Cidade,Estado)")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("Usuário criado com secesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com secesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, Operação cancelada!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:{conta["agencia"]}
            C/C:{conta["numero_conta"]}
            Titular:{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    valor = 0
    opcao = ""
    limite = 0
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    limite_saques = 3

    while opcao != 0:
        
        opcao = menu()

        if opcao == 1:
            depositar(float(input("Digite o valor a ser deposítado:R$")))

        elif opcao == 2:
            sacar(float(input("Digite o valor a ser sacado:R$")))

        elif opcao == 3:
            print("=====Extrato=====\n")
            print(extrato)
            print("Saldo na Conta R${:.2f}".format(saldo))

        elif opcao == 4:
            criar_usuario(usuarios)
        
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            print("Programa Finalizado.")

        else:
            print("Operação inválida, Selecione novamente a operação desejada.")
main()