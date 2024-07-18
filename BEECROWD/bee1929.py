A, B, C, D = map(int, input().split())
triangulo = ""
lista = [A, B, C, D]

lista.sort()

if (lista[0] + lista[1]) > lista[2] or (lista[1] + lista[2]) > lista[3]:
     triangulo = "S"
elif (lista[0] + lista[1]) > lista[3] or (lista[2] + lista[0]) > lista[3]:
    triangulo = "S"
else:
    triangulo = "N"

print(triangulo)


