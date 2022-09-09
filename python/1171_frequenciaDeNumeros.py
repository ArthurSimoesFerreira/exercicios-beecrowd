N = int(input())
contador = 1
numeros = []
for _ in range (N):
    num = int(input())
    numeros.append(num)
numeros.sort()
for i in range (0, len(numeros)):
    if i == len(numeros) - 1:
        if numeros[i] == numeros[i-1]:
            print(f"{numeros[i]} aparece {contador} vez(es)")
        else:
            print(f"{numeros[i]} aparece 1 vez(es)")
    elif numeros[i] == numeros[i+1]:
        contador += 1
    else:
        print(f"{numeros[i]} aparece {contador} vez(es)")
        contador = 1
        continue
    