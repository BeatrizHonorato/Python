import random
import time
secreto = random.randint(1,5)

print("Vou pensar em um numero de 1 a 5. Tente adivinhar...")

n1 = int(input("Em que numero pensei? "))
print("PROCESSANDO...")
time.sleep(2)
if n1 == secreto:
    print("Voce acertou!")
else:
    print("Errou! Pensei no numero {}".format(secreto))
