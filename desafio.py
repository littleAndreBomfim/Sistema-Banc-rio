banco = """
d = Depositar ,
s = sacar ,
e = extrato ,
q = sair , 

Qual opreção você quer realizar?  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_de_saques = 3

while True:
    opcao = input(banco)

    if opcao == "d":
        valor = float(input("Qual o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        else:
            print("O valor é inválido! Digite novamente")
    elif opcao == "s":
        valor = float(input("Qual o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_de_saques

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("Limite Excedido.")
        elif excedeu_saques:
            print("Operação não permitida. Número de saques foi excedido")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque de R${valor:.2f}\n"
        else:
            print("O valor é inválido! Digite novamente")
    elif opcao == "e":
        print("\n ~~~~~~~~~~~~~~~~~~~~~~Extrato~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif opcao == "q":
        break
    else:
        print("Opção inválida. Tente novamente.")
