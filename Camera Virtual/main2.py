import numpy as np
import matplotlib.pyplot as plt
from transformacoes import Transformacao as trf

def menu(id):
    menu = (('1. Manipular o objeto\n2. Manipular a câmera\n3. Modificar projeção\n4. Modificar mapeamento\n5. Visualizar objeto', 11),
            ('1.1. Translação\n1.2. Escala\n1.3. Rotação em X\n1.4. Rotação em Y\n1.5. Rotação em Z', 20),
            ('2.1. Translação\n2.2. Rotação em X\n2.3. Rotação em Y\n2.4. Rotação em Z',30),
            ('3.1. Projeção perspectiva\n3.2. Projeção paralela',40),
            ('4.1. Window\n4.2. Viewport',50))
    
    
    
    print(menu[id][0])
    op = int(input('Opcao: '))
    if op == 1:
        ang = float(input('Angulo: '))
        for i in piramide:
            trf.rotacaoZ(i, 45)

def atualizar():
    plt.clf()
    fig = plt.figure(figsize=(4, 4),frameon=False)
    ax = plt.axes(projection='3d')
    ax.set_axis_off()    
    fig.add_axes(ax)
    cor_linha = 'black'

    piramide = np.array([[0.0,0.0,0.5,1.0],
                [-0.5,-0.5,-0.5,1.0],
                [0.5,-0.5,-0.5,1.0],
                [-0.5,0.5,-0.5,1.0],
                [0.5,0.5,-0.5,1.0],
                ])

    topo = piramide[0]
    ie = piramide[1]
    id = piramide[2]
    se = piramide[3]
    sd = piramide[4]

    plt.plot([topo[0],ie[0]],[topo[1],ie[1]],[topo[2],ie[2]])
    plt.plot([topo[0],id[0]],[topo[1],id[1]],[topo[2],id[2]])
    plt.plot([topo[0],se[0]],[topo[1],se[1]],[topo[2],se[2]])
    plt.plot([topo[0],sd[0]],[topo[1],sd[1]],[topo[2],sd[2]])

    plt.plot([se[0],sd[0]],[se[1],sd[1]],[se[2],sd[2]])
    plt.plot([id[0],sd[0]],[id[1],sd[1]],[id[2],sd[2]])
    plt.plot([se[0],ie[0]],[se[1],ie[1]],[se[2],ie[2]])
    plt.plot([id[0],ie[0]],[id[1],ie[1]],[id[2],ie[2]])
    #plt.show()
    plt.savefig('x.jpg',transparent=True)

#inicializacao
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

#pontos da piramide
piramide = np.array([[0.0,0.0,0.5,1.0],
                [-0.5,-0.5,-0.5,1.0],
                [0.5,-0.5,-0.5,1.0],
                [-0.5,0.5,-0.5,1.0],
                [0.5,0.5,-0.5,1.0],
                ])

#matriz modelo

# turn off/on axis
plt.axis('off')   
atualizar()

# menu(0)
# while True:
#     op = int(input('opcao'))
#     if op == 0:
#         break
#     menu(op)
#     plt.savefig('x.jpg')
    #plt.show()
# show the graph