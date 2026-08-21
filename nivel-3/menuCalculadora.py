opcao = 1

while opcao != 0:
    print ("==== MENU DA CALCULADORA ====")
    print ("1. SOMA")
    print ("2. SUBTRAÇÃO")
    print ("3. MULTIPLICAÇÃO")
    print ("4. DIVISÃO")
    print ("0. SAIR")

    opcao = int(input("SELECIONE A OPÇÃO\n"))

    if opcao == 0:
        print ("PROGRAMA ENCERRADO!")
    elif opcao < 0:
        print ("OPÇÃO INVÁLIDA")
    elif opcao > 4:
        print ("OPÇÃO INVÁLIDA")
    elif opcao == 1:
        num1 = int(input("INSIRA O NÚMERO PARA SOMA\n"))
        num2 = int(input("INSIRA O SEGUNDO NÚMERO PARA SOMA\n"))
        soma = num1 + num2
        print (f"Resultado da soma {soma}")
    elif opcao == 2:
        num1 = int(input("INSIRA O NÚMERO PARA A SUBTRAÇÃO\n"))
        num2 = int(input("INSIRA O SEGUNDO NÚMERO PARA A SUBTRAÇÃO \n"))
        subtracao = num1 - num2
        print (f"Resultado da subtração {subtracao}")
    elif opcao == 3:
        num1 = int(input("INSIRA O NÚMERO PARA A MULTIPLICAÇÃO\n"))
        num2 = int(input ("INSIRA O SEGUNDO NÚMERO PARA A MULTIPLICAÇÃO\n"))
        mutiplicacao = num1 * num2
        print (f"Resultado de multiplicação {mutiplicacao}")
    elif opcao == 4:
        num1 = int(input("INSIRA O NÚMERO PARA A DIVISÃO\n"))
        num2 = int(input("INSIRA O SEGUNDO NÚMERO PARA A DIVISÃO\n"))
        if num2 == 0:
            print("ERRO! NÃO É POSSÍVEL DIVIDIR POR 0")
        else:
            divisao = num1/num2
            print(f"Resultado da divisão {divisao}")