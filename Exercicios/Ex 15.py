#Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado .Calcule o preço a pagar, sabendo que o carro custa por R$ 60 por dia e R$0,15 POR km rodado.

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos KM rodados? "))
pago = dias * 60
print("O total a pagaré de R${.:2f}".format(pago))