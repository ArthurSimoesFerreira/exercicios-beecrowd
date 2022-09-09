teste = 1
while True:
    partidas = int(input())
    if partidas == 0:
        break
    print("Teste", teste)
    nome1 = input()         # Pego nome do participante 1 (par)
    nome2 = input()          # Pego nome do participante 2 (ímpar)
    for i in range(partidas):
        A, B = map(int, input().split())
        if ((A + B) % 2) == 0:  # Caso a divisão por 2 tenha resto 0, a soma é par
            print(nome1)
        else:
            print(nome2)
    print()
    teste += 1
