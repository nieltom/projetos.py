import random
valor_aleatorio = random.randint(1,50)
acertou = False
while acertou == False:
 chute = int(input("chute um valor de 1 a 50 : ")) 
 if chute > valor_aleatorio:
    print ("chute foi maior que valor gerado")
 elif chute < valor_aleatorio:
    print("chute foi menor que valor gerado")
 elif chute == valor_aleatorio:
    acertou = True
    print("\033[94mAcertou mizeraviii!!!!")
   

