def Fib(num):
    v = [0,1]
    for i in range(2,num+1):
        f = v[i-1] + v[i-2]
        v.append(f)
    return(v[num])
        
N = int(input())
for teste in range(N):
    num = int(input())
    f = Fib(num)
    print(f"Fib({num}) = {f}")
    