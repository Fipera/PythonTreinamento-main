T = int(input())

caso = 1

while caso <= T:
    raj_win = f"Caso #{caso}: Raj trapaceou!"
    sheldon_win = f"Caso #{caso}: Bazinga!"
    empate = f"Caso #{caso}: De novo!"
    sheldon_hand, raj_hand = map(str, input().split())
    if sheldon_hand == "pedra":
        if raj_hand == "pedra":
            print(empate)
        elif raj_hand == "papel":
            print(raj_win)
        elif raj_hand == "tesoura":
            print(sheldon_win)
        elif raj_hand == "lagarto":
            print(sheldon_win)
        else:
            print(raj_win)

    elif sheldon_hand == "papel":
        if raj_hand == "pedra":
            print(sheldon_win)
        elif raj_hand == "papel":
            print(empate)
        elif raj_hand == "tesoura":
            print(raj_win)
        elif raj_hand == "lagarto":
            print(raj_win)
        else:
            print(sheldon_win)

    elif sheldon_hand == "tesoura":
        if raj_hand == "pedra":
            print(raj_win)
        elif raj_hand == "papel":
            print(sheldon_win)
        elif raj_hand == "tesoura":
            print(empate)
        elif raj_hand == "lagarto":
            print(sheldon_win)
        else:
            print(raj_win)

    elif sheldon_hand == "lagarto":
        if raj_hand == "pedra":
            print(raj_win)
        elif raj_hand == "papel":
            print(sheldon_win)
        elif raj_hand == "tesoura":
            print(raj_win)
        elif raj_hand == "lagarto":
            print(empate)
        else:
            print(sheldon_win)

    elif sheldon_hand == "Spock":
        if raj_hand == "pedra":
            print(sheldon_win)
        elif raj_hand == "papel":
            print(raj_win)
        elif raj_hand == "tesoura":
            print(sheldon_win)
        elif raj_hand == "lagarto":
            print(raj_win)
        else:
            print(empate)

    caso += 1

    