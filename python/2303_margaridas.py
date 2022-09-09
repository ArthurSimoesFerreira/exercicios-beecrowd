L, C, M, N = map(int, input().split())
plantacao = []
for _ in range(L):
    linha = list(map(int, input().split()))
    plantacao.append(linha)

soma = 0
somaNova = 0
for l in range(0,L,M):
    for k in range(0,C,N):
        for i in range(0,M):
            for j in range(k,k+1):
                somaNova += sum(plantacao[i+l][j:j+N])
        if somaNova > soma:
            soma = somaNova
        somaNova = 0
print(soma)