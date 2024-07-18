A, B, C = map(int, input().split())
desceuAB = A - B
desceuBC = B - C
subiuBA = B - A
subiuCB = C - B


if A == B:
    if C > B:
        print(":)")
    else:
        print(":(")

elif A > B:
    if B > C:
        if desceuAB > desceuBC:
            print(":)")
        else:
            print(":(")

    elif B == C or C > B:
        print(":)")

elif B > A:
    if B >= C:
        print(":(")

    elif C > B:
        if subiuCB >= subiuBA:
            print(":)")
        else:
            print(":(")