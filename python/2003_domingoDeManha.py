while True:
    try:
        horario = input()
        minutos = ((int( horario[0])) * 60) + (int(horario[2 : 4]))
        atraso = (minutos - (8*60)) + 60
        if atraso <= 0:
            print("Atraso maximo: 0")
        else:
            print("Atraso maximo: %d" %atraso)
    except EOFError:
        break