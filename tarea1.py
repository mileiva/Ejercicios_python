def triangulo(n):
    """
    for i in range(1,n+1) -> hacemos un bucle entre el 1 y el numero introducido
    " "*(n-i) -> añade los espacios al inicio
    "*"*(i+i-1) -> por cada valor entre el 1 y n+1, devolvemos la cantidad de asteriscos
    [] -> el resultado lo devuelve dentro de un array
    "\n".join() -> divide el array en una cadena separando cada elemento con un \n (salto de linea)
    """
    return "\n".join([" "*(n-i)+"*"*(i+i-1) for i in range(1,n+1)])
 
numero=int(input("indica un numero: "))
print(triangulo(numero))