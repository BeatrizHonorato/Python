#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
media = (n1+n2)/2

print("Primeira nota {}, segunda nota {}".format(n1,n2))
print("A média das notas {}".format(media))