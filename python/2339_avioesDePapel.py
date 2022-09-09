C,P,F = map(int, input().split())
folhas = C * F
if folhas > P:
    print("N")
else:
    print("S")