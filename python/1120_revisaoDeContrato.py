digito, numero =  input().split()
while digito != "0" and numero != "0":
    lista = []
    for i in range(len(numero)):
        lista.append(numero[i])
    qntd = len(lista)
    j = 0
    while j < qntd:
        if lista[j] == digito:
            lista.pop(j)
            qntd -= 1
        else:
            j += 1
    if len(lista) == 0:
        print(0)
    elif len(lista) >= 2 and lista[0] == "0" and lista[1] == "0":
        qntd = len(lista)
        k = 0
        while k < qntd:
            if qntd == 1 or lista[k] != "0":
                break
            else:
                lista.pop(k)
                qntd -= 1
        print("".join(lista))
    else:
        print("".join(lista))
    digito, numero = input().split()
    