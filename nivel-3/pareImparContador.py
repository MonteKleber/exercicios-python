quantNumero = int(input("Quantos números deseja informar ou digite 0 para sair: \n"))
contador = 0
par = 0
impar = 0

if quantNumero == 0:
    print ("PROGRAMA ENCERRADO!")
elif quantNumero < 0:
    print ("ERRO! O NÚMERO INFORMADO É NEGATIVO")
else:
    while contador < quantNumero:
        contador +=1
        num = int(input("Informe o número: \n"))
        resultado = num % 2
        if resultado == 0:
            par += 1
        else:
            impar += 1
    print (f"A quantidade de números pares: {par}\n")
    print (f"A quantidade de números impares é: {impar}")
