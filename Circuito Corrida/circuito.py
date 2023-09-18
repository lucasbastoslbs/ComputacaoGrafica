from matplotlib import pyplot as plt
import numpy as np
import random

"""
Utilizando curvas de Bezier e Hermite, construa um algoritmo que gere um circuito de corrida 3D totalmente aleatório.
O circuito deve ser composto de, pelo menos, 2 curvas de Bezier e 2 curvas de Hermite. 
Procure fazer com que o algoritmo gere circuitos com curvas o mais suaves possíveis.
"""
#config
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def bezier(P0,P1,P2,P3):
    t=0
    while t<=1:
        a = (1-t)*(1-t)*(1-t)
        b = 3*(1-t)*(1-t)*t
        c = 3*(1-t)*t*t
        d = t*t*t

        P = a*P0 + b*P1 + c*P2 + d*P3
        ax.scatter(P[0], P[1], P[2],color='black')
        t+=0.05

def hermite(P0,M1,M2,P2):
    t=0
    while t<=1:
        a = 2*t*t*t-3*t*t+1
        b = t*t*t-2*t*t+t
        c = -2*t*t*t+3*t*t
        d = t*t*t-t*t
        P = a*P0 + b*M1 + c*P2 + d*M2
        ax.scatter(P[0],P[1],P[2],color='black')
        t+=0.05

pontos = [np.array([2,2,2])]
#valor minimo deve ser 4 para manter pelo menos 2 de cada metodo
ciclos = 7
qtd_pontos = (ciclos*2)+ciclos

#gera os pontos aleatorios
for p in range(1,qtd_pontos):
    xr,yr,zr = random.randint(-10,10),random.randint(-10,10),random.randint(-10,10)
    x,y,z = pontos[p-1][0]+xr,pontos[p-1][1]+yr,pontos[p-1][2]+zr
    pontos.append(np.array([x,y,z]))

idx = 0
alternar = True
#cria os trajetos entre os pontos agrupados de 4 em 4 ate o penultimo ciclo
for _ in range(ciclos-1):
    if alternar:
        bezier(pontos[idx],pontos[idx+1],pontos[idx+2],pontos[idx+3])
        alternar = False
    else:
        hermite(pontos[idx],pontos[idx+1],pontos[idx+2],pontos[idx+3])
        alternar = True
    ax.scatter(pontos[idx][0],pontos[idx][1],pontos[idx][2],color='yellow')
    idx+=3
#ultimo ponto para o primeiro
if ciclos%2==0:
    hermite(pontos[idx],pontos[idx+1],pontos[idx+2],pontos[0])
else:
    bezier(pontos[idx],pontos[idx+1],pontos[idx+2],pontos[0])
ax.scatter(pontos[idx][0],pontos[idx][1],pontos[idx][2],color='yellow')
plt.show()