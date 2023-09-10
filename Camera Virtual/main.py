from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('Câmera Virtual')
window.geometry('1024x600')

canvas = Canvas(
    window,
    height=500,
    width=500,
    )

canvas.pack()

img= ImageTk.PhotoImage(Image.open("x_form.jpg"))

canvas.create_image(250,250,image=img)
canvas.place(anchor='nw')
#objeto widgets
Label(text='Opções do objeto', border=1).place(x=700,y=10)
#translacao
otg_x = 520
otg_y = 40
otg_height = 10
otg_width = 150
otx = Scale(window,orient=HORIZONTAL,length=otg_width,width=otg_height,sliderlength=10,from_=-200,to=200,tickinterval=100, label='Tx')
otx.pack()
otx.place(x=otg_x,y=otg_y)

oty = Scale(window,orient=HORIZONTAL,length=otg_width,width=otg_height,sliderlength=10,from_=-200,to=200,tickinterval=100, label='Ty')
oty.pack()
oty.place(x=otg_x+160,y=otg_y)

otz = Scale(window,orient=HORIZONTAL,length=otg_width,width=otg_height,sliderlength=10,from_=-200,to=200,tickinterval=100, label='Tz')
otz.pack()
otz.place(x=otg_x+320,y=otg_y)

#escala
osg_x = 520
osg_y = 120
osg_height = 10
osg_width = 150
osx = Scale(window,orient=HORIZONTAL,length=osg_width,width=osg_height,sliderlength=10,from_=-20,to=20,tickinterval=10, label='Sx')
osx.pack()
osx.place(x=osg_x,y=osg_y)

osy = Scale(window,orient=HORIZONTAL,length=osg_width,width=osg_height,sliderlength=10,from_=-20,to=20,tickinterval=10, label='Sy')
osy.pack()
osy.place(x=osg_x+160,y=osg_y)

osz = Scale(window,orient=HORIZONTAL,length=osg_width,width=osg_height,sliderlength=10,from_=-20,to=20,tickinterval=10, label='Sz')
osz.pack()
osz.place(x=osg_x+320,y=osg_y)

#rotacao
org_x = 520
org_y = 200
org_height = 10
org_width = 150
orx = Scale(window,orient=HORIZONTAL,length=org_width,width=org_height,sliderlength=10,from_=-360,to=360,tickinterval=180, label='Rx')
orx.pack()
orx.place(x=org_x,y=org_y)

ory = Scale(window,orient=HORIZONTAL,length=org_width,width=org_height,sliderlength=10,from_=-360,to=360,tickinterval=180, label='Ry')
ory.pack()
ory.place(x=org_x+160,y=org_y)

orz = Scale(window,orient=HORIZONTAL,length=org_width,width=org_height,sliderlength=10,from_=-360,to=360,tickinterval=180, label='Rz')
orz.pack()
orz.place(x=org_x+320,y=org_y)

# Initializing window

window.mainloop()