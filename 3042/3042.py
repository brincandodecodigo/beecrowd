# -*- coding: utf-8 -*-
def normaliza(nova_posicao):
    if nova_posicao == -1:
        return 2
    if nova_posicao == 3:
        return 0
    return nova_posicao


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
            esquerda = normaliza(antes - 1)
            direita = normaliza(antes + 1)
            proxima = caminho[i + 1]
            if proxima[esquerda] == '0' and abs(antes - esquerda) < abs(antes - direita):
                atual = esquerda
            else:
                atual = direita

        movs += abs(atual - antes)
    print(movs)
