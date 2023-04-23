def le_palavras(quantidade):
    palavras =[]
    for i in range(quantidade):
        palavras.append(input())
    return palavras

quantidade_palavras, linhas_matriz, colunas_matriz = [int(x) for x in input().split()]
palavras = le_palavras(quantidade_palavras)