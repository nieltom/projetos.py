velocidade_condutor = int(input("digite a velocidade em que estava  "))
velocidade_maxima = 80

if  int(velocidade_condutor) <= int(velocidade_maxima):
  print ("nao houve multa!!!")
elif  velocidade_condutor > velocidade_maxima and velocidade_condutor <= velocidade_maxima + 10:
 print ("multa leve!!!")
elif velocidade_condutor >= velocidade_maxima +11 and velocidade_condutor <= velocidade_maxima + 20:
 print ("multa grave!!!")
elif velocidade_condutor > velocidade_maxima + 20:
  print ("multa gravissima!!!")
