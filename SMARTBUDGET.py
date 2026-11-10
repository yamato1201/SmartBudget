print(" ================================SMARTBUDGET================================")

with open("saldo_atual.txt", "r") as arquivo:
    conteudo = arquivo.read()
    
    saldo_atual = float(conteudo)

historico_geral = []

while True:
    print("1 - Consultar saldo")
    print("2 - Adicionar saldo")
    print("3 - Registrar despesa")
    print("4 - ver histórico")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print(f"Saldo atual: {float(saldo_atual)}\n")


    elif opcao == 2:
        valor = float(input("digite o valor a ser adicionado: "))
        if valor <= 0:
            print("O valor do saldo não pode ser negativo ou 0.")
            continue
        with open("saldo_atual.txt", "w") as arquivo:
            saldo_atual = saldo_atual + valor
            arquivo.write(str(saldo_atual))
            print(str(saldo_atual))


    elif opcao == 3:
        despesa = float(input("digite o valor da despesa: "))
        descricao = input("digite a descrição da despesa: ")

        if despesa <= 0:
            print("O valor da despesa não pode ser negativo ou 0.")
            continue

        if despesa > saldo_atual:
            print("Você não possui saldo suficiente para realizar essa operação.")

        elif despesa <= saldo_atual:
            historico_geral.append(f"Despesa no valor de {float(despesa)} - Descrição: {str(descricao)}")
            print(f"Despesa registrada: {despesa}\n")
            with open("saldo_atual.txt", "w") as arquivo:
                saldo_atual = saldo_atual - despesa
                arquivo.write(str(saldo_atual))
        continue


    elif opcao == 4:
        if historico_geral == []:
            print("Nenhuma despesa registrada ainda.\n")
        print("Histórico geral:")
        for item in historico_geral:
            print(item)


    elif opcao == 5:
        print("Saindo do programa...")
        break
    if opcao < 1 or opcao > 5:
        print("opcão invalida, digite novamente")
        continue


