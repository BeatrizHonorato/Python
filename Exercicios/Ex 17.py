#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input("Insira a medida do cateto oposto: "))
ca = float(input("Insira a medida do cateto adjacente: "))
hip = hypot(ca,co)

print("A hipotenusa vai medir {:.2f}" .format(hip))