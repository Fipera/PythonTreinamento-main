N = int(input())


while N > 0:
    A, B = map(str, input().split())
    cabe = 0
    Ncabe = 0
    tamannhoB = len(B)

    if B > A:
        Ncabe = 1
    for x, i in enumerate(B):
        if i in A:
            cabe = 1
        else:
            Ncabe = 1

        
    if B[-1] == A[-1]:
        cabe = 1
    else:
        Ncabe = 1

    if Ncabe == 1:
        print("nao encaixa")
    else:
        print("encaixa")
    N-=1