#Escribe un algoritmo que lo ponga al revés un número 36 es 63

numero=int(input("Escriba un numero para ponerlo al revés"))

invertido=0

while(numero>=1):
    invertido=invertido*10+numero%10
    numero=int(numero/10)
    print(numero)

print("Invertido es " +str(invertido) )