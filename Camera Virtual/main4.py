import numpy as np
import math
import matplotlib.pyplot as plt

#limites da window
xminw = -5
yminw = -5
xmaxw = 0
ymaxw = 0

#limites da viewport
xminv = 0
yminv = 0
xmaxv = 400
ymaxv = 400

def desenhaLinha(p1x, p1y, p2x, p2y):
    point1 = [p1x, p1y]
    point2 = [p2x, p2y]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, color='black')

#1) Modelagem do objeto - X
#1 2   9 10
#    4
#  3   6
#    5
#7 8   11 12
x_form = np.array([[-2.0,1.5,0.5, 1.0] ,
[-1.0,1.5,0.5, 1.0] ,
[-0.5,0.0,0.5, 1.0] ,
[0.0,0.5,0.5, 1.0]  ,
[0.0,-0.5,0.5, 1.0] ,
[0.5,0.0,0.5, 1.0]  ,
[-2.0,-1.5,0.5, 1.0],
[-1.0,-1.5,0.5, 1.0],
[1.0,1.5,0.5, 1.0]  ,
[2.0,1.5,0.5, 1.0]  ,
[1.0,-1.5,0.5, 1.0] ,
[2.0,-1.5,0.5, 1.0] ,
#parte de traz
[-2.0,1.5,-0.5, 1.0] ,
[-1.0,1.5,-0.5, 1.0] ,
[-0.5,0.0,-0.5, 1.0] ,
[0.0,0.5,-0.5, 1.0]  ,
[0.0,-0.5,-0.5, 1.0] ,
[0.5,0.0,-0.5, 1.0]  ,
[-2.0,-1.5,-0.5, 1.0],
[-1.0,-1.5,-0.5, 1.0],
[1.0,1.5,-0.5, 1.0]  ,
[2.0,1.5,-0.5, 1.0]  ,
[1.0,-1.5,-0.5, 1.0] ,
[2.0,-1.5,-0.5, 1.0] ])

# print("\nCoordenadas do modelo")
# mostraPontos(p1, p2 ,p3 ,p4 ,p5 ,p6 ,p7 ,p8)

#a. Matriz de transformação do modelo
#translação
tx = 0
ty = 0
tz = 0
translacao = np.array([
    [1, 0, 0, tx],
    [0, 1, 0, ty],
    [0, 0, 1, tz],
    [0, 0, 0, 1]
])

#escala
sx = 1
sy = 1
sz = 1
escala = np.array([
    [sx, 0, 0, 0],
    [0, sy, 0, 0],
    [0, 0, sz, 0],
    [0, 0, 0, 1]    
])

#rotacao em x
angx = math.radians(0)
rotx = np.array([
    [1, 0, 0, 0],
    [0, math.cos(angx), -math.sin(angx), 0],
    [0, math.sin(angx), math.cos(angx), 0],
    [0, 0, 0, 1]    
])

#rotacao em y
angy = math.radians(0)
roty = np.array([
    [math.cos(angy), 0, math.sin(angy), 0],
    [0, 1, 0, 0],
    [-math.sin(angy), 0, math.cos(angy), 0],
    [0, 0, 0, 1]    
])

#rotacao em z
angz = math.radians(0)
rotz = np.array([
    [math.cos(angz), -math.sin(angz), 0, 0],
    [math.sin(angz), math.cos(angz), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]    
])

rotacao = rotz.dot(roty.dot(rotx))

matrizModelo = escala.dot(rotacao.dot(translacao))

#2) Coordenadas do mundo
pu = []
for p in x_form:
    pu.append(matrizModelo.dot(p))
# print("\nCoordenadas do mundo")
# mostraPontos(p1u, p2u ,p3u ,p4u ,p5u ,p6u ,p7u ,p8u)

#translação da câmera
txCam = 0
tyCam = 0
tzCam = -10
#é a cena que se move em torno da câmera
translacaoCam = np.array([
    [1, 0, 0, -txCam],
    [0, 1, 0, -tyCam],
    [0, 0, 1, -tzCam],
    [0, 0, 0, 1]
])

#rotação da câmera
#rotacao em y
angyCam = 0
angyCam = math.radians(-angyCam)
rotyCam = np.array([
        [math.cos(angyCam), 0, math.sin(angyCam), 0],
        [0, 1, 0, 0],
        [-math.sin(angyCam), 0, math.cos(angyCam), 0],
        [0, 0, 0, 1]    
])

matrizVisualizacao = rotyCam.dot(translacaoCam)

#3) Coordenadas de visualização
pv = []
for u in pu:
    pv.append(matrizVisualizacao.dot(u))
# print("\nCoordenadas de visualização")
# mostraPontos(p1v, p2v ,p3v ,p4v ,p5v ,p6v ,p7v ,p8v)

#c. Matriz de projeção
#projeção perspectiva
fovy = math.radians(80.0)
aspect = 1.0
zNear = 0.1
zFar = 100

a = 1/(math.tan(fovy/2) * aspect)
b = 1/(math.tan(fovy/2))
c = (zFar+zNear)/(zNear-zFar)
d = (2*(zFar*zNear))/(zNear-zFar)

matrizProjecao = np.array([
    [a, 0, 0, 0],
    [0, b, 0, 0],
    [0, 0, c, d],
    [0, 0, -1, 0]
])

pp = []
for v in pv:
    pp.append(matrizProjecao.dot(v))
#4) Coordenadas de projeção

#divide os pontox (x,y,z,w) por w, para que o w volte a ser 1
for i in range(len(pp)):
    pp[i] = pp[i]/pp[i][3]

# print("\nCoordenadas de projeção")
# mostraPontos(p1p, p2p ,p3p ,p4p ,p5p ,p6p ,p7p ,p8p)

#define os limites da janela onde os pontos serão renderizados
plt.xlim(350, 450)
plt.ylim(350, 450)

#d. Mapeamento
# print("\nMapeamento")
pmx = []
pmy = []
for p in pp:
    x = (((p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
    y = (((p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
    pmx.append(x)
    pmy.append(y)

#1 2   9 10
#    4
#  3   6
#    5
#7 8   11 12

#desenha as linhas que formam o X - frente
desenhaLinha(pmx[0], pmy[0], pmx[2], pmy[2] )
desenhaLinha(pmx[2], pmy[2], pmx[6], pmy[6] )
desenhaLinha(pmx[6], pmy[6], pmx[7], pmy[7] )
desenhaLinha(pmx[7], pmy[7], pmx[4], pmy[4] )
desenhaLinha(pmx[4], pmy[4], pmx[10], pmy[10] )
desenhaLinha(pmx[10], pmy[10], pmx[11], pmy[11] )
desenhaLinha(pmx[11], pmy[11], pmx[5], pmy[5] )
desenhaLinha(pmx[5], pmy[5], pmx[9], pmy[9] )
desenhaLinha(pmx[9], pmy[9], pmx[8], pmy[8] )
desenhaLinha(pmx[8], pmy[8], pmx[3], pmy[3] )
desenhaLinha(pmx[3], pmy[3], pmx[1], pmy[1] )
desenhaLinha(pmx[1], pmy[1], pmx[0], pmy[0])

##desenha as linhas que formam o X - frente-traz
for i in range(12):
    desenhaLinha(pmx[i], pmy[i], pmx[i+12], pmy[i+12] )

#desenha as linhas que formam o X - tras
desenhaLinha(pmx[0+12], pmy[0+12], pmx[2+12], pmy[2+12] )
desenhaLinha(pmx[2+12], pmy[2+12], pmx[6+12], pmy[6+12] )
desenhaLinha(pmx[6+12], pmy[6+12], pmx[7+12], pmy[7+12] )
desenhaLinha(pmx[7+12], pmy[7+12], pmx[4+12], pmy[4+12] )
desenhaLinha(pmx[4+12], pmy[4+12], pmx[10+12], pmy[10+12] )
desenhaLinha(pmx[10+12], pmy[10+12], pmx[11+12], pmy[11+12] )
desenhaLinha(pmx[11+12], pmy[11+12], pmx[5+12], pmy[5+12] )
desenhaLinha(pmx[5+12], pmy[5+12], pmx[9+12], pmy[9+12] )
desenhaLinha(pmx[9+12], pmy[9+12], pmx[8+12], pmy[8+12] )
desenhaLinha(pmx[8+12], pmy[8+12], pmx[3+12], pmy[3+12] )
desenhaLinha(pmx[3+12], pmy[3+12], pmx[1+12], pmy[1+12] )
desenhaLinha(pmx[1+12], pmy[1+12], pmx[0+12], pmy[0+12])

#plt.show()
plt.axis('off')
plt.savefig('x_form.jpg')