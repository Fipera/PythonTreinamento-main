while True:

    D, N = map(str, input().split())
    novo_N = ''
    tem = 0

    if N == '0' and D == '0':
        break

    for i in N:
        if i != D:
            novo_N += i
            tem = 1

    if tem == 0:
        print(0)
    else:
        print(int(novo_N))