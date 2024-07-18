while True:    
    N = int(input())
    matriz = []

    if N % 2 != 0:
          N2 = N - 1
    else:
          N2 = N

    for i in range(1, N + 1):
        linha = []
        for j in range(1, N + 1):
                linha.append(1)
        
        matriz.append(linha)


    for i in range(len(matriz)):
         for j in range(len(matriz)):
            
                 matriz[i][j] = N2

    for i in range(len(matriz)):
        print(matriz[i])
                 
              