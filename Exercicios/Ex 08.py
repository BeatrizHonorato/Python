#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

n1 = float(input("Digite a distancia em metros:"))
print("A média de {:.2f} corresponde a".format(n1))
km = n1 * 0.001
hm = n1*0.01
dam = n1*0.1
dm = n1*10
cm =n1*100
mm = n1*1000

print("{} KM".format(km))
print("{} HM".format(hm))
print("{:.2f} DAM".format(dam))
print("{} DM".format(dm))
print("{} CM".format(cm))
print("{} MM".format(mm))