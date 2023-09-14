n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))
n3 = int(input("Insira o terceiro numero: "))

if n1 == n2 :
    print("Numeros iguais")
elif n2 == n3 :
    print("Numeros iguais")
elif n1 == n3 :
    print("Numeros iguais")
elif n1 > n2:
    print("Numero {} é maior que o numero {}".format(n1, n2))
elif n1 < n2:
    print("Numero {} é menor que o numero {}".format(n1, n2))
elif n2 > n3:
    print("Numero {} é maior que o numero {}".format(n2, n3))
elif n2 < n3:
    print("Numero {} é menor que o numero {}".format(n2, n3))