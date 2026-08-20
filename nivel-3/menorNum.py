quantNum = int(input("Insira a quantidade de números que você deseja comparar ou digite 0 para sair \n"))
contador = 1

if quantNum == 0:
    print ("Programa encerrado!")
elif quantNum < 0:
    print ("Erro! Não é possível comparar uma quantidade de números negativos")
else:
    num1 = int(input("Informe um número:\n"))
    menor = num1
    while quantNum > contador:
        contador += 1
        num2 = int(input("Informe um número\n"))
        if num2 < menor:
            menor = num2
    print(f"O menor número é: {menor}")