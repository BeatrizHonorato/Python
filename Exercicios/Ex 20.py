#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteados.

from random import shuffle

nome1 = str(input("Insira o primeiro nome do aluno: "))
nome2 = str(input("Insira o segundo nome do aluno: "))
nome3 = str(input("Insira o terceiro nome do aluno: "))
nome4 = str(input("Insira o quarto nome do aluno: "))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print("A ordem da apresentação será ")
print(lista)