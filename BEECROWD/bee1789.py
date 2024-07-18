while True:
    try:
        L = int(input())
        velocidades = []
        nivel1 = 0
        nivel2 = 0
        nivel3 = 0
        velocidades = list(map(int, input().split()))

        for i in range(L):
            if velocidades[i] < 10:
                nivel1 = 1
            elif velocidades[i] >= 10 and velocidades[i] < 20:
                nivel2= 1
            elif velocidades[i] >= 20:
                nivel3 = 1

        if nivel3 == 1:
            print(3)
        elif nivel2 == 1:
            print(2)
        else:
            print(1)
    except EOFError:
        break
            