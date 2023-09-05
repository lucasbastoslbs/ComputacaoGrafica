import numpy as np
import matplotlib.pyplot as plt
from transformacoes import Transformacao

def menu(id):
    menu = (('1. Manipular o objeto\n2. Manipular a câmera\n3. Modificar projeção\n4. Modificar mapeamento\n5. Visualizar objeto', 11),
            ('1.1. Translação\n1.2. Escala\n1.3. Rotação em X\n1.4. Rotação em Y\n1.5. Rotação em Z', 20),
            ('2.1. Translação\n2.2. Rotação em X\n2.3. Rotação em Y\n2.4. Rotação em Z',30),
            ('3.1. Projeção perspectiva\n3.2. Projeção paralela',40),
            ('4.1. Window\n4.2. Viewport',50))
    
    print(menu[id][0])

#inicializacao
fig = plt.figure(figsize=(4, 4))
ax = plt.axes(projection='3d')
piramide = np.array([[0.0,0.0,1.0,1.0],
                [-1.0,-1.0,-1.0,1.0],
                [1.0,-1.0,-1.0,1.0],
                [-1.0,1.0,-1.0,1.0],
                [1.0,1.0,-1.0,1.0],
                ])

topo = piramide[0]
ie = piramide[1]
id = piramide[2]
se = piramide[3]
sd = piramide[4]

plt.plot([topo[0],ie[0]],[topo[1],ie[1]],[topo[2],ie[2]],color='black')
plt.plot([topo[0],id[0]],[topo[1],id[1]],[topo[2],id[2]],color='black')
plt.plot([topo[0],se[0]],[topo[1],se[1]],[topo[2],se[2]],color='black')
plt.plot([topo[0],sd[0]],[topo[1],sd[1]],[topo[2],sd[2]],color='black')

plt.plot([se[0],sd[0]],[se[1],sd[1]],[se[2],sd[2]],color='black')
plt.plot([id[0],sd[0]],[id[1],sd[1]],[id[2],sd[2]],color='black')
plt.plot([se[0],ie[0]],[se[1],ie[1]],[se[2],ie[2]],color='black')
plt.plot([id[0],ie[0]],[id[1],ie[1]],[id[2],ie[2]],color='black')
# turn off/on axis
plt.axis('off')

menu(0)
while True:
    op = int(input('opcao'))
    if op == 0:
        break
    menu(op)
# show the graph
#plt.savefig('z.jpg')
plt.show()