#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tintas necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
tint = area/2

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²".format(larg,alt,area))
print("Para pintar essa parede, voce precisará de {} de tinta".format(tint))