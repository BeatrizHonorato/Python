historico_transacoes = []  # Lista para armazenar as transações
saldo = 0.00

cadastro = input("Deseja se cadastrar? S/s ou N/n: ")

if cadastro == "S" or cadastro == "s":
    print("==============Cadastro====================")
    Digitoconta = input("Cadatre a sua conta, terá que ter 6 digitos: ")
    Digitosenha = input("Cadastre a senha, terá que ter 4 digitos: ")

    if len(Digitoconta) == 6 and len(Digitosenha) == 4:
        print("Cadastro efetuado com sucesso")
    else:
        print("Digitos da CONTA e SENHA incorretos")
else:
    print("Operação de cadastro cancelada")

while True:

    def deposito():
        global saldo
        print("DEPOSITO")
        print("Saldo: {}".format(saldo))

        depositar = float(input("Insira o valor: "))
        saldo_antes = saldo  # Salva o saldo antes da operação
        saldo += depositar  # Atualiza o saldo conforme o depósito realizado
        saldo_depois = saldo  # Salva o saldo após a operação
        historico_transacoes.append((1, saldo_antes, saldo_depois))  # Adiciona à lista de transações
        print('Saldo atual: {}'.format(saldo))


    def cheque():
        global saldo
        print("CHEQUE")
        print("Saldo: {}".format(saldo))

        DepositoCheque = float(input("Insira o saldo do cheque: "))
        saldo_antes = saldo  # Salva o saldo antes da operação
        saldo += DepositoCheque  # Atualiza o saldo conforme o depósito de cheque realizado
        saldo_depois = saldo  # Salva o saldo após a operação
        historico_transacoes.append((2, saldo_antes, saldo_depois))  # Adiciona à lista de transações
        print("Saldo atual: {}".format(saldo))


    def saque():
        global saldo
        print("SAQUE")
        print("Saldo: {}".format(saldo))

        sacar = float(input("Valor do saque: "))
        saldo_antes = saldo  # Salva o saldo antes da operação
        saldo -= sacar  # Atualiza o saldo conforme o saque realizado
        saldo_depois = saldo  # Salva o saldo após a operação
        historico_transacoes.append((3, saldo_antes, saldo_depois))  # Adiciona à lista de transações
        print("Saldo atual: {}".format(saldo))


    def pagamento():
        global saldo
        print("PAGAMENTO")
        print("Saldo: {}".format(saldo))

        pagar = float(input("Valor do pagamento: "))
        saldo_antes = saldo  # Salva o saldo antes da operação
        saldo -= pagar  # Atualiza o saldo conforme o pagamento realizado
        saldo_depois = saldo  # Salva o saldo após a operação
        historico_transacoes.append((4, saldo_antes, saldo_depois))  # Adiciona à lista de transações
        print("Saldo atual: {}".format(saldo))


    # Agora o dicionário contém apenas as funções, sem os parênteses
    switch = {
        1: deposito,
        2: cheque,
        3: saque,
        4: pagamento
    }

    opcao = int(input("Escolha uma opção (1 - Depósito, 2 - Cheque, 3 - Saque, 4 - Pagamento): "))
    if opcao in switch:
        switch[opcao]()  # Chama a função associada à opção escolhida
    else:
        print("Opção inválida")

    continuar = input("Deseja realizar outra operação? S/s para sim, qualquer outra tecla para sair: ")
    if continuar.lower() != "s":
        break

# Imprimir histórico de transações
print("\nHistórico de transações:")
for transacao in historico_transacoes:
    opcao, saldo_antes, saldo_depois = transacao
    print(f"Operação: {opcao}, Saldo antes: {saldo_antes:.2f}, Saldo depois: {saldo_depois:.2f}")
