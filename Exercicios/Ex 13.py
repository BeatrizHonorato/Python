#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

n1 = float(input("Qual é o salario do funcionario?"))

porc = n1*15/100
result = n1 + porc

print("Um funcionario que ganhava {}, com 15% de aumento, passa a receber {:.2f} ".format(n1,result))