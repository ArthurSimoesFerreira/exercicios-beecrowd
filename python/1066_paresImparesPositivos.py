numeros_pos = 0
numeros_neg = 0
numeros_par = 0
numeros_imp = 0
for i in range(5):
    num = int(input())
    if num > 0:
        numeros_pos += 1
    elif num < 0:
        numeros_neg += 1
    if num % 2 == 0:
        numeros_par += 1
    else: 
        numeros_imp += 1
print(f"{numeros_par} valor(es) par(es)")
print(f"{numeros_imp} valor(es) impar(es)")
print(f"{numeros_pos} valor(es) positivo(s)")
print(f"{numeros_neg} valor(es) negativo(s)")