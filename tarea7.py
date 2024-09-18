"""Saber si un numero es perfecto"""

def es_numero_perfecto(numero):
    if numero<1:
        return False
    suma=0
    for i in range(1, numero):
       if numero%i==0:
        suma+=i
    return suma==numero

numero=int(input("Ingrese numero: "))
if(es_numero_perfecto(numero)):
    print("Es numero perfecto")
else:
    print("No es número perfecto")
