import numpy as np
import math

class Transformacao:

    def translacao(self, ponto):
        tx = float(input('Tx: '))
        ty = float(input('Ty: '))
        tz = float(input('Tz: '))
        aux = np.array([[1.0,0.0,0.0,tx],
                        [0.0,1.0,0.0,ty],
                        [0.0,0.0,1.0,tz],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)

    def escala(self, ponto):
        sx = float(input('Sx: '))
        sy = float(input('Sy: '))
        sz = float(input('Sz: '))
        aux = np.array([[sx,0.0,0.0,0.0],
                        [0.0,sy,0.0,0.0],
                        [0.0,0.0,sz,0.0],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)

    def rotacaoX(self, ponto):
        ang = float(input('Angulo para X (em °): '))
        aux = np.array([[1.0,0.0,0.0,0.0],
                        [0.0,math.cos(ang),-math.sin(ang),0.0],
                        [0.0,math.sin(ang),math.cos(ang),0.0],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)
    
    def rotacaoY(self, ponto):
        ang = float(input('Angulo para Y (em °): '))
        aux = np.array([[math.cos(ang),0.0,math.sin(ang),0.0],
                        [0.0,1.0,0.0,0.0],
                        [-math.sin(ang),0.0,math.cos(ang),0.0],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)
    
    def rotacaoZ(self, ponto):
        ang = float(input('Angulo para Z (em °): '))
        aux = np.array([[math.cos(ang),-math.sin(ang),0.0,0.0],
                        [math.sin(ang),math.cos(ang),0.0,0.0],
                        [0.0,0.0,1.0,0.0],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)