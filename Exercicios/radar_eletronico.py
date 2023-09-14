velocidade = float(input("Insira a velocidade do automovel: "))

multa = (velocidade - 80) * 7

if velocidade <= 80 :
    print("Velocidade {} dentro do limite".format(velocidade))
elif velocidade > 80 :
    print("VELOCIDADE: {}".format(velocidade))
    print("Voce foi multato, multa é de {}".format(multa))


