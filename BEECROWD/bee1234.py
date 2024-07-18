

frase = input()
nova_frase = ''
x = 0

for y, i in enumerate(frase):
    if i == " ":
        nova_frase += i
    else:
        try:
            int(i)
            str(i)
            nova_frase += i
        except:

            iMenor = i.lower()
            iMaior = i.upper()
            
            if y == 0 or x == 2:
                nova_frase += iMaior
                x = 1 # proximo é minusculo
            elif x == 1:
                nova_frase += iMenor
                x= 2 # proximo é maiusculo

print(nova_frase)
