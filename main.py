from gl import *
from math import pi


glInit()
glCreateWindow(1024, 1024)

glClearColor(1, 1, 1)
glClear()
color = (0, 0, 1)

# fondo
glFondo("models_proyecto/texturas/fondo")

# objeto 1 (mascara 1)
objeto = "models_proyecto/mask1"
textura = "models_proyecto/texturas/mask1"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, 0.2, 0.5)
scale = (2, 2, 2)
rotate = (0, pi/2, 0)
glIntensidadLuz(0.9)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 2 (mascara 2)
objeto = "models_proyecto/mask2"
textura = "models_proyecto/texturas/mask2"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, 0.2, -0.5)
scale = (2, 2, 2)
rotate = (0, pi/2, 0)
glIntensidadLuz(0.85)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 3 (mascara 3)
objeto = "models_proyecto/mask3"
textura = "models_proyecto/texturas/mask3"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (800, 0, -0.95)
scale = (0.4, 0.4, 0.4)
rotate = (0, pi/2, 0)
glIntensidadLuz(0.8)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 4 (tablas)
objeto = "models_proyecto/tablas"
textura = "models_proyecto/texturas/tablas"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (-500, -1, 1)
scale = (0.4, 0.4, 0.4)
rotate = (0, 0, pi/2)
glIntensidadLuz(5)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 5 (caja y barril)
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
glFinish("escena_final")
