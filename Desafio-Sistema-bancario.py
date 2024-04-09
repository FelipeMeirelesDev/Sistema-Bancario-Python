menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair
=>"""

valor = 0
opcao = ""
saldo = 0
limite = 0
extrato = ""
numero_saques = 0
limite_saques = 3

while opcao != "q":
        
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser deposítado:R$"))
        if valor > 0: 
            saldo = saldo + valor
            extrato = extrato + ("Depósito de R${:.2f}\n".format(valor))
        else:
            print("Operação falhou! O valor é inválido")

    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado:R$"))
        if numero_saques <= limite_saques:
            if valor <= saldo:
                saldo = saldo - valor
                extrato = extrato + ("Retirada de R${:.2f}\n".format(valor))
                numero_saques = numero_saques + 1
            else:
                print("Operação falhou! O valor do saque excede o limite.")
        else:
            (print("Operação falhou! Número máximo de saques excedido"))

    elif opcao == "e":
        print("=====Extrato=====\n")
        print(extrato)
        print("Saldo na Conta R${}".format(saldo))

    elif opcao == "q":
        print("Programa Finalizado.")

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    

