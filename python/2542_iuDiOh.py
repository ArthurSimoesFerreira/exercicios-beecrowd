while True:
    try:
        N = int(input())
        M, L = map(int, input().split())
        cartasM = [] 
        cartasL = []
        for i in range (M):
            atributoM = (input().split())
            cartasM.append(atributoM)
        for j in range (L):
            atributoL = (input().split())
            cartasL.append(atributoL)
        CM, CL = map(int, input().split())
        A = int(input())
        AM = int(cartasM[CM-1][A-1])
        AL = int(cartasL[CL-1][A-1])
        if AM == AL:
            print("Empate")
        elif AM > AL:
            print("Marcos")
        else:
            print("Leonardo")
    except EOFError:
        break
    
        