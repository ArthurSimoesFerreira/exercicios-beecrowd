N = int(input())
notas = list(map(int, input().split()))
notas.sort()
i = 0
mais_repetidos = 0
maior = 0
while i < N:
    repetidos = notas.count(notas[i])
    i = i + repetidos - 1
    if repetidos >= mais_repetidos:
        mais_repetidos = repetidos
        maior = notas[i]
    i += 1
print(maior)
