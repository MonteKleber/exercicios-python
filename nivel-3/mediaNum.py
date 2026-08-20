quantidadeNum = int(input("Informe a quantidade de números que você deseja inserir ou digite 0 para sair:\n"))
contador = 0
total = 0

if quantidadeNum > 0:

    while contador < quantidadeNum:
    
        num = float(input("Informe o número para o calculo:\n"))
        total += num #acumula os valores digitados pelo usuário
        contador += 1 #armazena a quantidade de vezes que a estrtura foi chamada

    media = total/quantidadeNum
    print(f"A média dos valores informados é: {media:.2f}") #utiliza :2.f para arredondar o resultado para apenas duas casas decimais

elif quantidadeNum == 0: #Estrutura de decisão que faz o usuário encerrar o programa
    print("Programa encerrado!")

elif quantidadeNum < 0: #Estrtura de decisão que mostra o erro caso o usuário tente usar o progrma com números negativos
    print("Erro! Não posso aceitar números negativos para a quantidade de números")