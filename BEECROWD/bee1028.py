N = int(input())


while N > 0:
    F1, F2 = map(int, input().split())
    if F1 < F2:
        menor = F1
        maior = F2
    else:
        menor = F2
        maior = F1

    
    while True:
        resto = maior % menor
        if resto == 0:
            mmc = menor
            break
        else:
            maior = menor
            menor = resto

    print(mmc)



    N-= 1
