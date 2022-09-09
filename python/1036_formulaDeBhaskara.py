import math
linha = input()
numeros = linha.split()
a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])
if a!=0 :
    delta = b**2 - 4 * a * c
    if delta >= 0:
        r1 = (-b + math.sqrt(delta)) / (2 * a)
        r2 = (-b - math.sqrt(delta)) / (2 * a)
        print("R1 = %1.5f"%r1)
        print("R2 = %1.5f"%r2)
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")