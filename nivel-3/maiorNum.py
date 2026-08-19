quantNum = int(input("Informe a quantidade de números ou digite 0 para sair: \n"))
contador = 1

if quantNum == 0:
    print("Programa Encerrado")
elif quantNum < 0:
    print("Erro! Não posso comparar uma quantidade negativa de números")
else:
    num1 = int(input("Informe um número: \n"))
    maior = num1
    while quantNum > contador:
        contador += 1
        num2 = int(input("Informe um número: \n"))
        if maior < num2:
            maior = num2
    print(f"O maior número informado é: {maior}")