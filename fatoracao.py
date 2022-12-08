numero = int(input("digite o nomero a ser fatorado"))
if numero > 0:
 fatorial = 1
for item in range(1,numero+1):
  fatorial = fatorial * item
  print(fatorial)
else :
  print("o numero deve ser positivo")