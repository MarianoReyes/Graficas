from gl import *
from math import pi


glInit()
glCreateWindow(1024, 1024)

glClearColor(1, 1, 1)
glClear()
color = (0, 0, 1)

# fondo
# glFondo("models_proyecto/texturas/fondo")

# objeto 1 (mascara 1)
objeto = "models_proyecto/caja_barril"
textura = "models_proyecto/texturas/caja_barril"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, -0.7, -0.5)
scale = (0.2, 0.2, 0.2)
rotate = (0, 2*pi/2, pi/20)
glIntensidadLuz(5)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)


# RENDER
glFinish("pruebas")
