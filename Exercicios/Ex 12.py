#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n1 = float(input("Qual é o preço do produto? "))

pert = n1*5/100
result = n1 - pert
print("O produto que custava {}, na promoção com desconto de 5% vai custar {:.2f}".format(n1,result))