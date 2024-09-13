menu = """
Digite:
[d] para Depositar
[s] para Sacar
[e] para Extrato
[x] para sair

"""
saldo = 0
limite = 500
extrato = ""
num_saque = 0
lim_saque = 3

while True:
    seleciona = input(menu)
    if seleciona == "d":
        valor = float(input("Valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else:
            print("Valor inválido.")
    elif seleciona == "s":
        valor = float(input("Digite o valor a ser sacado: "))
        sem_saldo = valor > saldo
        sem_limite = valor > limite
        sem_saque = num_saque >= lim_saque

        if 0 < valor <= saldo and valor <= limite and num_saque < lim_saque:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            num_saque += 1
        elif sem_saldo:
            print("Saldo Insuficiente.")
        elif sem_limite:
            print("Valor de Saque Excedido.")
        elif sem_saque:
            print("Limite de Saques Excedido.")
        else:
            print("Valor Inválido")   
    elif seleciona == "e":
        print(f"Saldo: R$ {saldo: .2f}")
        print("Extrato:")
        print(extrato if extrato else "Nenhuma transação realizada.")
    elif seleciona == "x":
        break
    else:
        print("Operação Inválida")
