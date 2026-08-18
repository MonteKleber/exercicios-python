numero = int(input ("Informe o número:\n")) #SOLICITA AO USUÁRIO QUE INFORME O NÚMERO
raiz = pow(numero, 0.5) #DETERMINA A RAIZ QUADRADA
cont = 0 #DEFINE UM CONTADOR
acum = 0 #DEFINE UM ACUMULADOR

while cont <= raiz: #ESTRUTURA CONDICIONAL PARA TESTAR OS VALORES
    cont = cont+ 1
    resultado = numero % cont #DIVIDE O NÚMERO QUE FOI DEFINIDO PELO USUÁRIO PELO CONTADOR 
    if resultado == 0: #SE O RESTO DA DIVISÃO FOR DIFERENTE DE 0 ENTÃO...
        acum += 1
if acum == 1: #CASO O ACUMULADOR SEJA IGUAL A 1 ENTÃO ELE EXIBE É QUE É UM NÚMERO PRIMO.
    print("O número é primo!")
else:
    print ("O número não é primo!")