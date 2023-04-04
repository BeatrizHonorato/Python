#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos,tan,sin,radians

angulo = float(input("Digita o angulo: "))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
seno = sin(radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo,seno))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo,cosseno))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(angulo,tangente))