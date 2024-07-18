frase1 = input()
frase2 = input()
frase3 = input()
frase1_limitada = []
frase2_limitada = []
frase3_limitada = []

print(frase1, frase2, frase3, sep="")
print(frase2, frase3, frase1, sep="")
print(frase3, frase1, frase2, sep="")


if len(frase1) >= 10:
    for i in range(10):
        frase1_limitada += frase1[i]
else:
    frase1_limitada = frase1


if len(frase2) >= 10:
    for i in range(10):
        frase2_limitada += frase2[i]
else:
    frase2_limitada = frase2

if len(frase3) >= 10:
    for i in range(10):
        frase3_limitada += frase3[i]
else:
    frase3_limitada = frase3


frase1_menor10 = "".join(frase1_limitada)
frase2_menor10 = "".join(frase2_limitada)
frase3_menor10 = "".join(frase3_limitada)


print(frase1_menor10, frase2_menor10, frase3_menor10, sep="")