C = int(input())

while C > 0:
    N, M = map(int, input().split())
    potencia = N ** M
    C -= 1
    qntd_digitos = len(str(potencia))
    print(qntd_digitos)