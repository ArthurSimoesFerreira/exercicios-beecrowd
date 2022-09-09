n1, n2, n3, n4 = map(float, input().split()) 
media = float((n1*2 + n2*3 + n3*4 + n4*1)/10)
print("Media: %1.1f" %media)
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:  
    print("Aluno em exame.")
    notaexame = float(input())
    print("Nota do exame: %1.1f" %notaexame)
    novamedia = float((notaexame + media)/2)
    if novamedia >= 5:
        print("Aluno aprovado.")
    elif novamedia < 5:
        print("Aluno reprovado.")
    print("Media final: %1.1f"%novamedia)
            