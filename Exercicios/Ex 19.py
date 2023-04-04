#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

lista = input("Insira o primeiro aluno: "), input("Insira o segundo aluno:"), \
        input("Insira o terceiro aluno: "), input("Insira o quarto aluno: ")
print("Alunos que irá participar do sorteio {}".format(lista))
print("Aluno que foi sorteado {}".format(choice(lista)))
