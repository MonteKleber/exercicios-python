numSecreto = 67
tentativaUsuario = int(input("Digite o número:\n")) #realiza a primeira pergunta ao usuário
quantidadeTentativa = 1

if numSecreto == tentativaUsuario:
    print ("Parabéns! Você acertou o número secreto!\n")
    print (f"Quantidade de tentativas: {quantidadeTentativa}")
else:
    while tentativaUsuario != numSecreto: #coloca a condição de que o loop só se encerra caso o usuário acertar o número
        if numSecreto < tentativaUsuario: #faz a comparação para determinar se o número informado é menor
            print ("O número secreto é menor!")
            
        elif numSecreto > tentativaUsuario: #ou maior
            print ("O número secreto é maior!")
        
        tentativaUsuario = int(input("Digite o número:\n"))
        quantidadeTentativa += 1
        if numSecreto == tentativaUsuario:
            print ("Parabéns! Você acertou o número secreto!")
            print (f"Quantidade de tentativas: {quantidadeTentativa}") #exibe uma mensagem de parabéns e informa quantos tentativas foram necessárias
    