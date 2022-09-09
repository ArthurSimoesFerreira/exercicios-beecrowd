vet = [None] * 20 
for i in range(20):
    vet[i] = int(input())
vet.reverse()
for j in range(20):
    print(f"N[{j}] = {vet[j]}")