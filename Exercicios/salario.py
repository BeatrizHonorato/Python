salario = float(input("Informe o salario bruto: "))

aut_10 = (salario * 10)/100

aut_15 = (salario * 15)/100

if salario >= 1250:
    print("O aumento do salario é {} é de 10%".format(aut_10 ))
elif salario < 1250:
    print("O aumento do salario é {} é de 15%".format(aut_15 ))
