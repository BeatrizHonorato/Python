#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt
n1 = int(input("Digite um numero:"))
d = n1 * 2
t = n1 *3
r = sqrt(n1)

print("O dobro de {} vale {}".format(n1,d))
print("O triplo de {} vale {}".format(n1,t))
print("A raiz quadrada de {} é igual a {:.2f}".format(n1,r))