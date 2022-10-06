from gl import *
from math import pi


glInit()
glCreateWindow(1024, 1024)

glClearColor(1, 1, 1)
glClear()
color = (0, 0, 1)

# fondo
# glFondo("models_proyecto/texturas/fondo")

objeto = "models_proyecto/pilar"
textura = "models_proyecto/texturas/pilar"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (-500, 0, 0)
scale = (10, 10, 10)
rotate = (0, pi/2, 0)
glIntensidadLuz(0.85)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

""" # objeto 1 (mascara 1)
objeto = "models_proyecto/mask1"
textura = "models_proyecto/texturas/mask1"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, 0, 0.5)
scale = (2, 2, 2)
rotate = (0, pi/2, 0)
glIntensidadLuz(0.85)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 2 (mascara 2)
objeto = "models_proyecto/mask2"
textura = "models_proyecto/texturas/mask2"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, 0, -0.5)
scale = (2, 2, 2)
rotate = (0, pi/2, 0)
glIntensidadLuz(0.85)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color) """


# RENDER
glFinish("escena_final")
