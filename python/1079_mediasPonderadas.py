n = int(input())
for i in range(n):
    n2,n3,n5 = map(float, input().split())
    media = ((n2*2)+(n3*3)+(n5*5))/10
    print(f"{media:.1f}")