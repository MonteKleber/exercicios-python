senha = 'python123' #define uma senha
contador = 0

while contador < 3:
    tentativa = input("Digite sua senha: \n") #solicita que o usuário faça uma tentativa
    if tentativa == senha: #caso a senha seja a certa, então retorna a mensagem e sai do while
        print ("Senha correta!") 
        break
    else:
        print ("Senha incorreta!") #caso a senha seja errada adiciona mais um no contador
        contador += 1
        if contador == 3:
            print("Número de tentativas chegou ao limite!")