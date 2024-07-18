linha1 = input()
linha2 = input()
valorA1 = 0
valorA2 = 0

for i in linha1:
    if i == 'a':
        valorA1 += 1

for i in linha2:
    if i == 'a':
        valorA2 += 1

if valorA2 > valorA1:
    print("no")
else:
    print("go")
