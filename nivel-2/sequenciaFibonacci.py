termo = int(input("Quantos termos você deseja que seja gerado para a sequencia de fibonacci:\n")) #SOLICITA QUE O USUARIO INFORME A QUANTIDADE DE TERMOS
#váriaveis
contador = 1
sequencia = 0
num1 = 0
num2 = 1

if termo > 1:
    print (sequencia)
    print (num2)
    contador += 1
    while contador < termo:
        contador += 1
        sequencia = num1 + num2
        num1 = num2
        num2 = sequencia 
        print (sequencia)
elif termo == 1: #verifica se a quantidade de termos solicitadas pelo usuário é 1
    print (sequencia)
elif termo == 0: #retorna a mensagem de erro ao usuário caso ele queira 0 termos
    print ("Erro: Não posso gerar 0 termos para a sequencia de fibonacci")
else: #retorna a mensagem de erro que não é possível organizar uma sequencia de fibonacci com números negativos
    print ("Erro: Não é possível gerar a sequência de fibonacci com uma quantidade de termos negativa!")

