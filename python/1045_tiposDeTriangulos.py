n1, n2, n3 = map(float, input().split()) #peço os valores e separo pelos espaços entres eles
Lista = [n1, n2, n3]
Lista.sort() #ponho a lista em ordem crescente
A = Lista[2] #escolho o maior
B = Lista[1]
C = Lista[0]
if A >= (B + C):
    print("NAO FORMA TRIANGULO") 
else:
    if (A**2) == (B**2 + C**2):
        print("TRIANGULO RETANGULO")
    if (A**2) > (B**2) + (C**2):
        print("TRIANGULO OBTUSANGULO")
    if (A**2) < (B**2) + (C**2):
        print("TRIANGULO ACUTANGULO")
    if (A == B != C) or (A == C != B) or (B == C != A):
        print("TRIANGULO ISOSCELES")
    if A == B == C: 
        print ("TRIANGULO EQUILATERO")