N = int(input())

while N > 0:
    X = int(input())
    resposta = "Prime"

    for i in range(2, int(X ** 0.5) + 1):
        if X % i == 0:
            resposta = "Not Prime"
            break
    N -= 1
    print(resposta)