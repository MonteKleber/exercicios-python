numero = int(input ("Informe o número:\n")) #SOLICITA AO USUÁRIO QUE INFORME O NÚMERO
cont = 0 #DEFINE UM CONTADOR
acum = 0 #DEFINE UM ACUMULADOR

if (numero == 0 or numero == 1):
    print ("O número não é primo!")
elif (numero == 2):
    print ("O número é primo")
elif (numero < 0):
    print ("Erro: Não existem números primos negativos!")
else:
    raiz = pow(numero, 0.5) #DETERMINA A RAIZ QUADRADA
    while cont <= raiz: #ESTRUTURA CONDICIONAL PARA TESTAR OS VALORES
        cont = cont+ 1
        resultado = numero % cont #DIVIDE O NÚMERO QUE FOI DEFINIDO PELO USUÁRIO PELO CONTADOR 
        if resultado == 0: #SE O RESTO DA DIVISÃO FOR IGUAL A 0...
            acum += 1
    if acum == 1: #CASO O ACUMULADOR SEJA IGUAL A 1 ENTÃO ELE EXIBE É QUE É UM NÚMERO PRIMO.
        print("O número é primo!")
    elif acum > 1:
        print ("O número não é primo!") 