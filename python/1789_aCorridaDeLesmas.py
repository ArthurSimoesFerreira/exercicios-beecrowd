try:
    while True:
        num_lesmas = int(input())
        lesmas = list(map(int, input().split()))
        velocidade_maxima = max(lesmas)
        if velocidade_maxima < 10:
            print("1")
        elif 10 < velocidade_maxima  and velocidade_maxima < 20:
            print("2")
        else:
            print("3")
except EOFError:
    pass