billetes=[100,50,20,10,5,1]

dinero= int(input("Igrese la cantidad de dinero:"))

for billete in billetes:
    if dinero>=billete:
        cantidad=dinero//billete
        print("Existe " +str(cantidad)+ ( ' moneda ' if dinero < 5 else ' billetes ')+ " de "+str(billete)+ ( ' dólar ' if dinero < 5 else ' dólares '))
        dinero=dinero%billete