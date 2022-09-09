maior = 0
for i in range(100):
    n = int(input())
    if n > maior:
        maior = n 
        indice = i+1
print(maior)
print(indice)