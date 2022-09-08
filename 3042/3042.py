# -*- coding: utf-8 -*-
def normaliza(atual, posicao_invalida, posicao_valida, alteracao):
    if atual == posicao_invalida:
        return posicao_valida
    return atual + alteracao


while (True):
    m = int(input())
    if m == 0:
        break
    caminho = []
    for aux in range(m):
        caminho.append(input().split())

    atual = 1
    movs = 0
    for i in range(len(caminho)):
        if caminho[i][atual] == '0':
            continue

        antes = atual
        if caminho[i].count('0') == 1:
            atual = caminho[i].index('0')
        else:
            esquerda = normaliza(antes, 0, 2, -1)
            direita = normaliza(antes, 2, 0, 1)
            proxima = caminho[i + 1]
            if proxima[esquerda] == '0' and abs(antes - esquerda) < abs(antes - direita):
                atual = esquerda
            else:
                atual = direita

        movs += abs(atual - antes)
    print(movs)
