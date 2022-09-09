linhas, colunas = map(int, input().split())
matriz = []
verificador = False
for lin in range(linhas):
    linha = list(map(int, input().split()))
    matriz.append(linha)
for i in range(1,linhas-1):
    for j in range(1,colunas-1):
        if matriz[i][j] == 42:
            if matriz[i][j-1] == 7 and matriz[i][j+1] == 7:
                if matriz[i+1][j-1] == 7 and matriz[i+1][j] == 7 and matriz[i+1][j+1] == 7:
                    if matriz[i-1][j-1] == 7 and matriz[i-1][j] == 7 and matriz[i-1][j+1] == 7:
                        verificador = True
                        print(f"{i+1} {j+1}")
                        break
if not verificador:
    print("0 0")