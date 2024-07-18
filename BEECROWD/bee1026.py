import sys

for line in sys.stdin:
    A, B = [int(z) for z in line.split()]
    resto = 0
    A32 = []
    B32 = []
    soma = []
    i = 0
    j = 0
    k = 0
    total = 0

    while A != 1 or B != 1:
        if A != 1:
            resto = A % 2
            A = A // 2
            A32.append(resto)
        if B != 1:
            resto = B % 2
            B = B // 2
            B32.append(resto)
        
    A32.append(1)
    B32.append(1)

    while len(A32) < 32 or len(B32) < 32:
        if len(A32) < 32:
            A32.append(0)
        if len(B32) < 32:
            B32.append(0)


    

    for j in range(len(A32)):
        if (A32[j] == 1 and B32[j] == 1) or (A32[j] == 0 and B32[j] == 0):
            soma.append(0)
        else:
            soma.append(1)
            total += 2 ** j
            

    soma.reverse()


    print(total)