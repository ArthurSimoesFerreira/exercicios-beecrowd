def contar_presenca(lista_nomes, lista_presencas):
    reprovados = ""
    for i, j in zip(lista_nomes, lista_presencas):
        qntd_presente = j.count("P")
        qntd_de_m = j.count("M")
        qntd_de_aulas = len(j)
        frequencia = (qntd_presente/(qntd_de_aulas - qntd_de_m))*100
        if frequencia < 75:
            reprovados += i + " "
    return reprovados


def main():
    # Pegar numero de estudantes
    num_estudantes = int(input())

    for _ in range(num_estudantes):
        qntd_nomes = int(input())

        # Pegar nomes e presencas
        lista_nomes = list(map(str, input().split()))
        lista_presencas = list(map(str, input().split()))

        # Ver quem foi reprovado por falta
        reprovados = contar_presenca(lista_nomes, lista_presencas)
        
        # Tirando espaços à direita
        reprovados = reprovados.rstrip()
        print(reprovados)


if __name__ == '__main__':
    main()
