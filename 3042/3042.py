# -*- coding: utf-8 -*-
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
        elif antes == 1:
            if caminho[i + 1][0] == '0':
                atual = 0
            else:
                atual = 2
        elif antes == 0:
            if caminho[i + 1][1] == '0':
                atual = 1
            else:
                atual = 2
        elif antes == 2:
            if caminho[i + 1][1] == '0':
                atual = 1
            else:
                atual = 0
        movs += abs(atual - antes)
    print(movs)