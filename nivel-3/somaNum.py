numero = int (input("Insira um número:\n"))
contador = 0
soma = 0


if numero >= 0:
    while contador < numero:
        contador += 1
        soma = contador + soma 
    print (soma)