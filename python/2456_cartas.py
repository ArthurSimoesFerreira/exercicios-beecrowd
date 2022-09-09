numeros = list(map(int, input().split()))
if numeros == sorted(numeros):
    print("C")
elif numeros == sorted(numeros, reverse=True):
    print("D")
else: 
    print("N")
    