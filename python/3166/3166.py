def le_palavras(quantidade):
    palavras =[]
    for i in range(quantidade):
        palavras.append(input())
    return palavras


def le_conteudo(linhas_matriz, colunas_matriz):
    conteudo = []
    for i in range(linhas_matriz):
        linha = list(input())
        conteudo.append(linha)
    return conteudo

quantidade_palavras, linhas_matriz, colunas_matriz = [int(x) for x in input().split()]
palavras = le_palavras(quantidade_palavras)
conteudo = le_conteudo(linhas_matriz, colunas_matriz)