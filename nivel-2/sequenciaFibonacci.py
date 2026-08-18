termo = int(input("Quantos termos você deseja que seja gerado para a fibra de fibonacci:\n")) #SOLICITA QUE O USUARIO INFORME A QUANTIDADE DE TERMOS
#váriaveis
contador = 0
sequencia = 0
num1 = 0
num2 = 1

while contador < termo:
    contador += 1
    sequencia = num1 + num2
    num2 = num1
    num1 = sequencia 
    print (sequencia)