from tkinter import *
from main3 import gera_imagem
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
window = Tk()
window.title('Câmera Virtual')
window.geometry('1024x680')

def get_matriz_text(mat):
    texto = ''
    for i in mat:
        for j in i:
            texto += str(j)[:5] + '\t'
        texto += '\n' 
    return texto
    # return str(mat[0])+'\n'+str(mat[1])+'\n'+str(mat[2])+'\n'+str(mat[3])

def toggle_projecao():
    if(radio_toggled.get() == 'perspectiva'):  
        prl_xLeft_entry.configure(state='readonly')
        prl_xRight_entry.configure(state='readonly')
        prl_yBottom_entry.configure(state='readonly')
        prl_yTop_entry.configure(state='readonly')
        prl_zNear_entry.configure(state='readonly')
        prl_zFar_entry.configure(state='readonly')

        prs_fovy_entry.configure(state='normal')
        prs_aspect_entry.configure(state='normal')
        prs_zNear_entry.configure(state='normal')
        prs_zFar_entry.configure(state='normal')
    else:
        prl_xLeft_entry.configure(state='normal')
        prl_xRight_entry.configure(state='normal')
        prl_yBottom_entry.configure(state='normal')
        prl_yTop_entry.configure(state='normal')
        prl_zNear_entry.configure(state='normal')
        prl_zFar_entry.configure(state='normal')

        prs_fovy_entry.configure(state='readonly')
        prs_aspect_entry.configure(state='readonly')
        prs_zNear_entry.configure(state='readonly')
        prs_zFar_entry.configure(state='readonly')

    atualizar(0)

def atualizar(_):
    if(radio_toggled.get() == 'perspectiva'):
        projecao_params = [param.get() for param in prs]
    else:
        projecao_params = [param.get() for param in prl]

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

                'projecao': radio_toggled.get(),
                'projecao_params': projecao_params,

                'xminw' : xminw.get(),
                'yminw' : yminw.get(),
                'xmaxw' : xmaxw.get(),
                'ymaxw' : ymaxw.get(),
                'xminv' : xminv.get(),
                'yminv' : yminv.get(),
                'xmaxv' : xmaxv.get(),
                'ymaxv' : ymaxv.get(),
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
mat_visual_lbl.place(x=20, y=500)
mat_proj_lbl = Label(text='Matriz Projeção\n')
mat_proj_lbl.place(x=260, y=500)
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

#opcoes de projecao -----------

#paralela ----------
radio_toggled = StringVar()
perspectiva_radio = Radiobutton(window, value='perspectiva', text='Perspectiva',variable=radio_toggled,command=toggle_projecao)
perspectiva_radio.select()
perspectiva_radio.place(x=520, y=475)
prs = []
for _ in range(4):
    prs.append(DoubleVar())
prs[0].set(80)
prs[1].set(1)
prs[2].set(0.1)
prs[3].set(100)
prs_fovy_lbl = Label(window,text='fovy')
prs_fovy_lbl.place(x=520,y=500)
prs_fovy_entry = Entry(window,textvariable=prs[0],width=5)
prs_fovy_entry.place(x=560,y=500)
prs_aspect_lbl = Label(window,text='aspect')
prs_aspect_lbl.place(x=620,y=500)
prs_aspect_entry = Entry(window,textvariable=prs[1],width=5)
prs_aspect_entry.place(x=660,y=500)
prs_zNear_lbl = Label(window,text='zNear')
prs_zNear_lbl.place(x=720,y=500)
prs_zNear_entry = Entry(window,textvariable=prs[2],width=5)
prs_zNear_entry.place(x=760,y=500)
prs_zFar_lbl = Label(window,text='zFar')
prs_zFar_lbl.place(x=820,y=500)
prs_zFar_entry = Entry(window,textvariable=prs[3],width=5)
prs_zFar_entry.place(x=860,y=500)

# --- perspectiva
paralela_radio = Radiobutton(window, value='paralela', text='Paralela',variable=radio_toggled,command=toggle_projecao)
paralela_radio.place(x=520, y=530)
prl = []
for _ in range(6):
    prl.append(DoubleVar())
prl[0].set(-3)
prl[1].set(3)
prl[2].set(-3)
prl[3].set(3)
prl[4].set(0.1)
prl[5].set(100)
prl_xLeft_lbl = Label(window,text='xLeft')
prl_xLeft_lbl.place(x=520,y=560)
prl_xLeft_entry = Entry(window,textvariable=prl[0],width=5,state='readonly')
prl_xLeft_entry.place(x=560,y=560)
prl_xRight_lbl = Label(window,text='xRight')
prl_xRight_lbl.place(x=520,y=580)
prl_xRight_entry = Entry(window,textvariable=prl[1],width=5,state='readonly')
prl_xRight_entry.place(x=560,y=580)
prl_yBottom_lbl = Label(window,text='yBottom')
prl_yBottom_lbl.place(x=670,y=580)
prl_yBottom_entry = Entry(window,textvariable=prl[2],width=5,state='readonly')
prl_yBottom_entry.place(x=720,y=580)
prl_yTop_lbl = Label(window,text='yTop')
prl_yTop_lbl.place(x=670,y=560)
prl_yTop_entry = Entry(window,textvariable=prl[3],width=5,state='readonly')
prl_yTop_entry.place(x=720,y=560)
prl_zNear_lbl = Label(window,text='zNear')
prl_zNear_lbl.place(x=820,y=560)
prl_zNear_entry = Entry(window,textvariable=prl[4],width=5,state='readonly')
prl_zNear_entry.place(x=860,y=560)
prl_zFar_lbl = Label(window,text='zFar')
prl_zFar_lbl.place(x=820,y=580)
prl_zFar_entry = Entry(window,textvariable=prl[5],width=5,state='readonly')
prl_zFar_entry.place(x=860,y=580)

#----------------viewport e window -----------------
 #limites da window
xminw = DoubleVar()
yminw = DoubleVar()
xmaxw = DoubleVar()
ymaxw = DoubleVar()
xminw.set(-5)
yminw.set(-5)
xmaxw.set(0)
ymaxw.set(0)

#limites da viewport
xminv = DoubleVar()
yminv = DoubleVar()
xmaxv = DoubleVar()
ymaxv = DoubleVar()
xminv.set(0)
yminv.set(0)
xmaxv.set(400)
ymaxv.set(400)

viewport_xminv_lbl = Label(window,text='xminv')
viewport_xminv_lbl.place(x=20,y=600)
viewport_xminv_entry = Entry(window,textvariable=xminv,width=5)
viewport_xminv_entry.place(x=60,y=600)
viewport_xmaxv_lbl = Label(window,text='xmaxv')
viewport_xmaxv_lbl.place(x=20,y=620)
viewport_xmaxv_entry = Entry(window,textvariable=xmaxv,width=5)
viewport_xmaxv_entry.place(x=60,y=620)
viewport_yminv_lbl = Label(window,text='yminv')
viewport_yminv_lbl.place(x=120,y=620)
viewport_yminv_entry = Entry(window,textvariable=yminv,width=5)
viewport_yminv_entry.place(x=160,y=620)
viewport_ymaxv_lbl = Label(window,text='ymaxv')
viewport_ymaxv_lbl.place(x=120,y=600)
viewport_ymaxv_entry = Entry(window,textvariable=ymaxv,width=5)
viewport_ymaxv_entry.place(x=160,y=600)
Label(text='---- Viewport ----', border=1).place(x=60,y=640)

window_xminw_lbl = Label(window,text='xminw')
window_xminw_lbl.place(x=260,y=600)
window_xminw_entry = Entry(window,textvariable=xminw,width=5)
window_xminw_entry.place(x=300,y=600)
window_xmaxw_lbl = Label(window,text='xmaxw')
window_xmaxw_lbl.place(x=260,y=620)
window_xmaxw_entry = Entry(window,textvariable=xmaxw,width=5)
window_xmaxw_entry.place(x=300,y=620)
window_yminw_lbl = Label(window,text='yminw')
window_yminw_lbl.place(x=360,y=620)
window_yminw_entry = Entry(window,textvariable=yminw,width=5)
window_yminw_entry.place(x=400,y=620)
window_ymaxw_lbl = Label(window,text='ymaxw')
window_ymaxw_lbl.place(x=360,y=600)
window_ymaxw_entry = Entry(window,textvariable=ymaxw,width=5)
window_ymaxw_entry.place(x=400,y=600)
Label(text='---- Window ----', border=1).place(x=300,y=640)

# Initializing window
window.mainloop()