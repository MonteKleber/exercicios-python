numero = int(input("Digite um número: "))
fatorial = 1
contador = numero

if numero >= 0:
    while contador > 0:
            fatorial *= contador # *= é equivalente a: fatorial = fatorial * contador
            contador -= 1
    print(f"O fatorial de {numero} é {fatorial}")
else:
      print("Não existe fatorial para números negativos")