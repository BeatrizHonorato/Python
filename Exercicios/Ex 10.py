#Crie um prograama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$3,27

n1 = float(input("Quanto dinheiro voce tem na carteira?"))
s = n1/3.27

print("Com {} voce pode comprar US${:.2f}".format(n1,s))