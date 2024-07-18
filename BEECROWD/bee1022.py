N = int(input())
sinal = ""
4
while N > 0:
    N1, barra1, D1, op, N2, barra2, D2 = map(str, input().split())
    N1 = int(N1)
    N2 = int(N2)
    D1 = int(D1)
    D2 = int(D2)

    if op == "+":
        resultadoNumerador = (N1 * D2 + N2 * D1)
        resultadoDenominador = (D1 * D2)
    elif op == "-":
        resultadoNumerador = (N1 * D2 - N2 * D1)
        resultadoDenominador = (D1 * D2)

    elif op == "*":
        resultadoNumerador = (N1 * N2)
        resultadoDenominador = (D1 * D2)

    elif op == "/":
        resultadoNumerador = (N1 * D2)
        resultadoDenominador = (N2 * D1)


    if resultadoNumerador > resultadoDenominador:
        maior = resultadoNumerador
        menor = resultadoDenominador
    else:
        maior = resultadoDenominador
        menor = resultadoNumerador

    divisor = menor
    if divisor < 0:
        divisor *= -1
        sinal = "negativo"

    while divisor >= 0:
        if divisor == 0:
            resultadoNumeradorSimplificado = resultadoNumerador
            resultadoDenominadorSimplificado = resultadoDenominador
            break;

        elif (maior % divisor == 0 and menor % divisor == 0 and divisor > 1):
            if maior == resultadoNumerador:
                resultadoNumeradorSimplificado = maior / divisor
                resultadoDenominadorSimplificado = menor / divisor
            else:
                resultadoNumeradorSimplificado = menor / divisor
                resultadoDenominadorSimplificado = maior / divisor
           
            break;
        
        divisor -= 1



    resultadoNumeradorSimplificado = int(resultadoNumeradorSimplificado)
    resultadoDenominadorSimplificado = int(resultadoDenominadorSimplificado)

    print(f"{resultadoNumerador}/{resultadoDenominador} = {resultadoNumeradorSimplificado}/{resultadoDenominadorSimplificado}")
    

    

    N -= 1

    

