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

#canvas.create_rectangle(
#    10,10,490,490,
#    outline="#fb0",
#    )

img= ImageTk.PhotoImage(Image.open("z.jpg"))

canvas.create_image(250,250,image=img)
canvas.place(anchor='nw')
# Create a photoimage object of the image in the path
#image1 = Image.open(r"C:\Users\laboratorio\Desktop\ComputacaoGrafica\Camera Virtual\y.jpg")
# test = ImageTk.PhotoImage(image1)
#canvas.create_image(image1)

# label1.image = test

# label2 = tkinter.Label(text='wsize')
# # Position image
# label2.place(x=100,y=200)

# Initializing window

window.mainloop()