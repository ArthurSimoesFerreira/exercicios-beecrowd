while True:
    try:
        nota = float(input())
        if 0 <= nota <= 10:
            while True:
                nota2 = float(input())
                if 0 <= nota2 <= 10:
                    media = (nota + nota2)/2
                    print(f"media = {media:.2f}")
                    break
                else:
                    print("nota invalida")
                    continue
        else:
            print("nota invalida")
            continue
    except EOFError:
        break