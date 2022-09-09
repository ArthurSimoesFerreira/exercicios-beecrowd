linha = int(input())
operação = input()
soma = 0
for i in range(12):
    for j in range(12):
        numero = float(input())
        if i == linha:
            soma += numero
if operação == "M":
    media = soma/12
    print(f"{media:.1f}")
else:
    print(f"{soma:.1f}")