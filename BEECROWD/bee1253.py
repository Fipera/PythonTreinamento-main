alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nova_frase = ''

N = int(input())


while N > 0:
    frase = input()
    X = int(input())
    frase = frase.lower()

    for i in frase:
        indice_novo = alfabeto.index(i) - X
        if indice_novo < 0:
            indice_novo += 26
        
        nova_frase += (alfabeto[indice_novo])

    N-= 1

    nova_frase = nova_frase.upper()
    print(nova_frase)
    nova_frase = ''