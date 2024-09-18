matriz= [
    [ 1, 12, 13 ],
    [ 21, 22, 23 ],
    [ 31, 32, 33 ]
]
diagonalIzquierda = lambda m: [m[i][i] for i in range(len(m))]
diagonalDerecha = lambda m: [m[i][len(m)-1-i] for i in range(len(m))]
print(diagonalIzquierda(matriz)) 
print(diagonalDerecha(matriz))