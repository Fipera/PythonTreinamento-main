economias = 10
semana = 1
total_economizado = economias
 
while total_economizado < 320:
    semana += 1
    economias *= 2
    total_economizado += economias
    
print(semana)
print(total_economizado)
