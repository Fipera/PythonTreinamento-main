p = int(input())
valor = 0

while p > 0:
    id, q = map(int, input().split())
    if id == 1001:
        valor += q * 1.50
    elif id == 1002:
        valor += q * 2.50
    elif id == 1003:
        valor += q * 3.50
    elif id == 1004:
        valor += q * 4.50
    elif id == 1005:
        valor += q * 5.50
    
    p -= 1

print(f"{valor:.2f}")