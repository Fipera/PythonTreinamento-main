T = int(input())

while T > 0:
    B = int(input())
    aiDabriel, diDabriel, liDabriel = map(int, input().split())
    aiGuarte, diGuarte, liGuarte = map(int, input().split())
    
    if liDabriel % 2 == 0 and liGuarte % 2 == 0:
        valorGolpeDabriel = (aiDabriel + diDabriel) / 2 + B
        valorGolpeGuarte = (aiGuarte + diGuarte) / 2 + B
    elif liDabriel % 2 == 0:
        valorGolpeDabriel = (aiDabriel + diDabriel) / 2 + B
        valorGolpeGuarte = (aiGuarte + diGuarte) / 2
    elif liGuarte % 2 == 0:
        valorGolpeDabriel = (aiDabriel + diDabriel) / 2
        valorGolpeGuarte = (aiGuarte + diGuarte) / 2 + B
    else:
        valorGolpeDabriel = (aiDabriel + diDabriel) / 2
        valorGolpeGuarte = (aiGuarte + diGuarte) / 2

    if valorGolpeDabriel > valorGolpeGuarte:
        print("Dabriel")
    elif valorGolpeDabriel == valorGolpeGuarte:
        print("Empate")
    else:
        print("Guarte")

    T -= 1
        


    