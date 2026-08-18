contador = 0
numero = int(input("Insira o número para que consultar a tabuáda:\n")) #solicita a entrada de dados
multiplicador = 1
resultado = int

while contador <= 10:
    resultado = numero * multiplicador #realiza os calculos
    print (numero , 'x', multiplicador ,'=')
    print (resultado) #exibe a saída de dados
    multiplicador = multiplicador + 1
    contador = contador + 1