N = int(input())

while N > 0:
    x, y = map(int, input().split())
    rafael = (3 * x) ** 2 + y ** 2
    beto = 2*(x ** 2) + (5*y) ** 2
    carlos = (-1) * 100*x + y ** 3

    if rafael > beto and rafael > carlos:
        maior = "Rafael"
    elif beto > carlos and beto > rafael:
        maior = "Beto"
    else:
        maior = "Carlos"

    print(f"{maior} ganhou")


    N -= 1
