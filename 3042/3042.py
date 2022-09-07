# -*- coding: utf-8 -*-
while (True):
    m = int(input())
    if m == 0:
        break
    a = 'c'
    caminho = []
    for aux in range(m):
        i = input().split()
        l, c, r = i
        caminho.append([l, c, r])

    atual = 1
    mov = 0
    for i in range(len(caminho)):
        if i == m:
            break
        if caminho[i][atual] == '0':
            continue
        l = caminho[i][0]
        c = caminho[i][1]
        r = caminho[i][2]
        if atual == 1:
            mov += 1
            if l == '0' and r == '1':
                atual = 0
                continue
            elif l == '1' and r == '0':
                atual = 2            
                continue
            else:
                if caminho[i + 1][0] == '0':
                    atual = 0
                else:
                    atual = 2
        elif atual == 0:
            if c == '0' and r == '1':
                atual = 1
                mov += 1
                continue
            elif c == '1' and r == '0':
                atual = 2
                mov += 2
                continue
            else:
                if caminho[i + 1][1] == '0':
                    atual = 1
                    mov += 1
                    continue
                else:
                    atual = 2
                    mov += 2
                    continue
        elif atual == 2:
            if c == '0' and l == '1':
                atual = 1
                mov += 1
                continue
            elif c == '1' and l == '0':
                atual = 0
                mov += 2
                continue
            else:
                if caminho[i + 1][1] == '0':
                    atual = 1
                    mov += 1
                else:
                    atual = 0
                    mov += 2
    print(mov)