nota1 = float(input("Insira a primeira nota\n"))
nota2 = float(input ("Insira a segunda nota\n"))
nota3 = float(input ("Insira a terceira nota\n"))

somaNota = nota1 + nota2 + nota3 #soma das notas
mediaFinal = somaNota/3#calculo da média

print("A média final das notas infomradas é: ")
print (mediaFinal)

if mediaFinal >= 7:

    print ("Aluno Aprovado!")

if mediaFinal >=5 and mediaFinal < 7:
    
    print ("Aluno de recuperação")

if mediaFinal < 5:
    print ("Aluno reprovado")