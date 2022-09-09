N = int(input())
ida = 0
volta = 0
subidas = []
identificadores = []
for i in range(N):
    lista = list(map(int, input().split()))
    identificadores.append(lista[0])
    for j in range(1, lista[0]):
        dif = (lista[j+1] - lista[j])
        if dif > 0:
            ida += dif
        else:
            volta += -dif
    if ida < volta:
        subidas.append(ida)
    else:
        subidas.append(volta)
    ida = 0
    volta = 0
x = min(subidas)
indice = (subidas.index(x)) + 1
print(indice)