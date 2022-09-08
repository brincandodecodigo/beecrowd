# -*- coding: utf-8 -*-
def le_caminho(m):
    caminho = []
    for aux in range(m):
        i = input().split()
        l, c, r = i
        caminho.append([l, c, r])
    return caminho

while (True):
    m = int(input())
    if m == 0:
        break
    caminho = le_caminho(m)

    atual = 1
    movs = 0
    for i in range(len(caminho)):
        if i == m:
            break
        if caminho[i][atual] == '0':
            continue
        l = caminho[i][0]
        c = caminho[i][1]
        r = caminho[i][2]
        antes = atual
        if antes == 1:
            if l == '0' and r == '1':
                atual = 0
            elif l == '1' and r == '0':
                atual = 2            
            else:
                if caminho[i + 1][0] == '0':
                    atual = 0
                else:
                    atual = 2
        elif antes == 0:
            if c == '0' and r == '1':
                atual = 1
            elif c == '1' and r == '0':
                atual = 2
            else:
                if caminho[i + 1][1] == '0':
                    atual = 1
                else:
                    atual = 2
        elif antes == 2:
            if c == '0' and l == '1':
                atual = 1
            elif c == '1' and l == '0':
                atual = 0
            else:
                if caminho[i + 1][1] == '0':
                    atual = 1
                else:
                    atual = 0
        movs += abs(atual - antes)
    print(movs)
    