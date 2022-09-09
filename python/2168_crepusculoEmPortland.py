n = int(input())
matriz = []
seguranca = []
verificador = 0
for _ in range (n+1):
    linha = list(map(int, input().split()))
    matriz.append(linha)
for i in range(n):
    quadras = []
    for j in range(n):
        quadra = matriz[i][j:j+2] + matriz[i+1][j:j+2]
        if quadra.count(1) >= 2:
            quadras.append("S")
        else:
            quadras.append("U")
    seguranca.append(quadras)
for lin in range(n):
    for col in range(n):
        print(seguranca[lin][col], end="")
    print()