from tkinter import *
from main3 import gera_imagem
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')
window = Tk()
window.title('Câmera Virtual')
window.geometry('1024x600')

def get_matriz_text(mat):
    texto = ''
    for i in mat:
        for j in i:
            texto += str(j)[:8] + '\t'
        texto += '\n' 
    return texto
    # return str(mat[0])+'\n'+str(mat[1])+'\n'+str(mat[2])+'\n'+str(mat[3])

def atualizar(_):
    valores = {'otx': otx.get(),
               'oty': oty.get(),
               'otz': otz.get(),

               'osx': osx.get(),
               'osy': osy.get(),
               'osz': osz.get(),
               
               'orx': orx.get(),
               'ory': ory.get(),
               'orz': orz.get(),

               'ctx': ctx.get(),
               'cty': cty.get(),
               'ctz': ctz.get(),

               'crx': crx.get(),
               'cry': cry.get(),
               'crz': crz.get(),
               }
    plt.clf()
    mat_vis, mat_proj = gera_imagem(valores)
    fig.canvas.draw()
    mat_proj_lbl.config(text='Matriz Projeção\n'+get_matriz_text(mat_proj))
    mat_visual_lbl.config(text='Matriz Visualização\n'+get_matriz_text(mat_vis))

fig = plt.figure(figsize=[4.5,4.5])
plt.ion()
canvas = FigureCanvasTkAgg(fig, master = window)
plot_widget = canvas.get_tk_widget()
plot_widget.grid(column=0,row=0)

mat_visual_lbl = Label(text='Matriz Visualização\n')
mat_visual_lbl.place(x=20, y=475)
mat_proj_lbl = Label(text='Matriz Projeção\n')
mat_proj_lbl.place(x=260, y=475)
#objeto widgets ===================================================
Label(text='---------- Opções do objeto ---------- ', border=1).place(x=650,y=10)
#translacao
otg_x = 520
otg_y = 40
otg_height = 10
otg_width = 150
otx = Scale(window,orient=HORIZONTAL,length=otg_width,width=otg_height,sliderlength=10,from_=-200,to=200,tickinterval=100, label='Tx',command=atualizar)
otx.place(x=otg_x,y=otg_y)

oty = Scale(window,orient=HORIZONTAL,length=otg_width,width=otg_height,sliderlength=10,from_=-200,to=200,tickinterval=100, label='Ty',command=atualizar)
oty.place(x=otg_x+160,y=otg_y)

otz = Scale(window,orient=HORIZONTAL,length=otg_width,width=otg_height,sliderlength=10,from_=-200,to=200,tickinterval=100, label='Tz',command=atualizar)
otz.place(x=otg_x+320,y=otg_y)

#escala
osg_x = 520
osg_y = 120
osg_height = 10
osg_width = 150
osx = Scale(window,orient=HORIZONTAL,length=osg_width,width=osg_height,sliderlength=10,from_=-20,to=20,tickinterval=10, label='Sx',command=atualizar)
osx.set(1)
osx.place(x=osg_x,y=osg_y)

osy = Scale(window,orient=HORIZONTAL,length=osg_width,width=osg_height,sliderlength=10,from_=-20,to=20,tickinterval=10, label='Sy',command=atualizar)
osy.set(1)
osy.place(x=osg_x+160,y=osg_y)

osz = Scale(window,orient=HORIZONTAL,length=osg_width,width=osg_height,sliderlength=10,from_=-20,to=20,tickinterval=10, label='Sz',command=atualizar)
osz.set(1)
osz.place(x=osg_x+320,y=osg_y)

#rotacao
org_x = 520
org_y = 200
org_height = 10
org_width = 150
orx = Scale(window,orient=HORIZONTAL,length=org_width,width=org_height,sliderlength=10,from_=-360,to=360,tickinterval=180, label='Rx',command=atualizar)
orx.place(x=org_x,y=org_y)

ory = Scale(window,orient=HORIZONTAL,length=org_width,width=org_height,sliderlength=10,from_=-360,to=360,tickinterval=180, label='Ry',command=atualizar)
ory.place(x=org_x+160,y=org_y)

orz = Scale(window,orient=HORIZONTAL,length=org_width,width=org_height,sliderlength=10,from_=-360,to=360,tickinterval=180, label='Rz',command=atualizar)
orz.place(x=org_x+320,y=org_y)

#camera widgets ===========================================================
#objeto widgets
Label(text='---------- Opções da câmera ---------- ', border=1).place(x=650,y=280)
#translacao
ctg_x = 520
ctg_y = 300
ctg_height = 10
ctg_width = 150
ctx = Scale(window,orient=HORIZONTAL,length=ctg_width,width=ctg_height,sliderlength=10,from_=-200,to=200,tickinterval=100, label='Tx',command=atualizar)
ctx.place(x=ctg_x,y=ctg_y)

cty = Scale(window,orient=HORIZONTAL,length=ctg_width,width=ctg_height,sliderlength=10,from_=-200,to=200,tickinterval=100, label='Ty',command=atualizar)
cty.place(x=ctg_x+160,y=ctg_y)

ctz = Scale(window,orient=HORIZONTAL,length=ctg_width,width=ctg_height,sliderlength=10,from_=-200,to=200,tickinterval=100, label='Tz',command=atualizar)
ctz.set(-5)
ctz.place(x=ctg_x+320,y=ctg_y)

#rotacao
crg_x = 520
crg_y = 380
crg_height = 10
crg_width = 150
crx = Scale(window,orient=HORIZONTAL,length=crg_width,width=crg_height,sliderlength=10,from_=-360,to=360,tickinterval=180, label='Rx',command=atualizar)
crx.place(x=crg_x,y=crg_y)

cry = Scale(window,orient=HORIZONTAL,length=crg_width,width=crg_height,sliderlength=10,from_=-360,to=360,tickinterval=180, label='Ry',command=atualizar)
cry.place(x=crg_x+160,y=crg_y)

crz = Scale(window,orient=HORIZONTAL,length=crg_width,width=crg_height,sliderlength=10,from_=-360,to=360,tickinterval=180, label='Rz',command=atualizar)
crz.place(x=crg_x+320,y=crg_y)

# Initializing window

window.mainloop()