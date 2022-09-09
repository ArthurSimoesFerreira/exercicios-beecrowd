J, R = map(int, input().split())
pontos = list(map(int, input().split()))
lista = []
j = 0
cont = 0
soma = 0
for i in range(J-1, -1, -1):
    while j < len(pontos) - i:
        soma += pontos[j]
        j += J
    cont += 1
    lista.append(soma)
    j = cont
    soma = 0
pont_max = max(lista)
num = lista.count(pont_max)
if num > 1:
    lista.reverse()
    for k in range(len(lista)):
        if lista[k] == pont_max:
            print(J-k)
            break
else:
    print(lista.index(pont_max)+ 1)