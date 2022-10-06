from gl import *
from math import pi

objeto = "models_proyecto/mask1"
textura = "models_proyecto/texturas/mask1"

glInit()
glCreateWindow(1024, 1024)
glViewPort(0, 0, 1024, 1024)
glClearColor(1, 1, 1)
glClear()
color = (0, 0, 1)

glTexture(textura)

translate_factor = (0, 0, 0)
scale_factor = (4, 4, 4)
rotate = (0, pi/2, 0)

glLoadMMatriz(translate_factor, scale_factor, rotate)

# RENDER
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
generar_objeto(objeto, color)
glFinish("escena_final")
