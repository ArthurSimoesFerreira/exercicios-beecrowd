N = int(input())
alturas = list(map(int, input().split()))
verificador = 0
if N == 2:
    if alturas[0] != alturas[1]:
        verificador = 1
else:
    for i in range(1,N-1):
        if alturas[i-1]>alturas[i]<alturas[i+1] or alturas[i-1]<alturas[i]>alturas[i+1]:
            verificador = 1
        else:
            verificador = 0
            break
print(verificador)