import random

numero_a_adivinar= random.randint(1,15)

intentos=4

while(intentos>0 ):
   numero=int(input("Ingrese un número para adivinar entre el 1 y 15 "))
   if (numero==numero_a_adivinar):
      print("Usted adivino")
      break
   else:
        print("No acerto el número")
        intentos=intentos-1

print("El número era: "+str(numero_a_adivinar))