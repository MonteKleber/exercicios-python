num1 = int(input("informe um número\n"))
num2 = int(input("informe um número\n"))
num3 = int(input("informe um número\n"))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3:
    maior = num2
else:
    maior = num3
    
print(f"o maior número é: {maior}")