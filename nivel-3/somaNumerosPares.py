quantNumero = int(input("Informe a quantidade de números que você deseja que sejam somados ou digite 0 para finalizar\n"))
cont = 0
acum = 0

if quantNumero == 0: #verifica o que o usuário digitou, caso seja 0 ele encerra o programa
    print ("Programa encerrado!")
elif quantNumero < 0:
    print ("ERRO! A quantidade de números não pode ser negativa") #caso seja número seja negativo, retorna uma mensagem de erro ao usuário
else:
    while cont < quantNumero: #Cria um loop para que a instrução seja feita pela quantidade de vezes que o usuário requeriu
        cont += 1
        num = int(input("Informe o valor desejado:\n"))
        par = num % 2
        if par == 0: #Faz a verificação se o número é par ou impar
            acum += num #através de um acumulador soma todos os números
    print(f"A soma dos números pares é igual a: {acum}")
