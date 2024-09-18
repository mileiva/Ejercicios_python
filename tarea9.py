
numero=int(input("Ingrese un numero del 1 al 12 para mostrar tabla de multiplicar "))
if(numero<=0 or numero>12):
    print("ingrese un número valido")
else: 
  multiplicador=1  
  print("Tabla de multiplicar del "+str(numero))
  while(multiplicador<=12):
    print(str(numero)+" X "+str(multiplicador)+" = "+str(numero*multiplicador)) 
    multiplicador=multiplicador+1   