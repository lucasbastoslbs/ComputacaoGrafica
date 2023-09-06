import numpy as np
import math

class Transformacao:

    def translacao(ponto, tx, ty, tz):
        aux = np.array([[1.0,0.0,0.0,tx],
                        [0.0,1.0,0.0,ty],
                        [0.0,0.0,1.0,tz],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)

    def escala(ponto, sx, sy, sz):
        aux = np.array([[sx,0.0,0.0,0.0],
                        [0.0,sy,0.0,0.0],
                        [0.0,0.0,sz,0.0],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)

    def rotacaoX(ponto, ang):
        ang = math.radians(ang)
        aux = np.array([[1.0,0.0,0.0,0.0],
                        [0.0,math.cos(ang),-math.sin(ang),0.0],
                        [0.0,math.sin(ang),math.cos(ang),0.0],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)
    
    def rotacaoY(ponto, ang):
        ang = math.radians(ang)
        aux = np.array([[math.cos(ang),0.0,math.sin(ang),0.0],
                        [0.0,1.0,0.0,0.0],
                        [-math.sin(ang),0.0,math.cos(ang),0.0],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)
    
    def rotacaoZ(ponto, ang):
        ang = math.radians(ang)
        aux = np.array([[math.cos(ang),-math.sin(ang),0.0,0.0],
                        [math.sin(ang),math.cos(ang),0.0,0.0],
                        [0.0,0.0,1.0,0.0],
                        [0.0,0.0,0.0,1.0]])
        return aux.dot(ponto)