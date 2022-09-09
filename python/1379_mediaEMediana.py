a, b = map(int, input().split())
while (a!=0 and b!=0):
    A = min(a,b)
    B = max(a,b)
    C = 2*A - B
    print(C)
    a, b = map(int, input().split())