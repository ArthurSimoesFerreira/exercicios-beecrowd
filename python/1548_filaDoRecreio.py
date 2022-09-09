num_casos = int(input())
for _ in range(num_casos):
    permanecentes = 0
    num_alunos = int(input())
    notas = list(map(int, input().split()))
    ord_notas = sorted(notas, reverse=True)
    for i  in range(num_alunos):
        if notas[i] == ord_notas[i]:
            permanecentes += 1
    print(permanecentes)
    i = 0
