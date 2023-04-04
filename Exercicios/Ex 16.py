#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Exemplo Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

from math import trunc

n1 = float(input("Insira um numero: "))
print(trunc(n1))

