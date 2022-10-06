from gl import *
from math import pi


glInit()
glCreateWindow(1024, 1024)

glClearColor(1, 1, 1)
glClear()
color = (0, 0, 1)

# fondo
glFondo("models_proyecto/texturas/fondo")

# objeto 1 (locker)
objeto = "models_proyecto/locker"
textura = "models_proyecto/texturas/locker"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, -0.5, 0.4)
scale = (0.6, 0.6, 0.6)
rotate = (0, pi/9, 0)
glIntensidadLuz(3)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 2 (tablas)
objeto = "models_proyecto/tablas"
textura = "models_proyecto/texturas/tablas"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (-500, -0.3, 0.5)
scale = (0.3, 0.3, 0.3)
rotate = (0, pi/3, pi/2)
glIntensidadLuz(10)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 3 (caja y barril)
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

# objeto 4 (humano)
objeto = "models_proyecto/humano"
textura = "models_proyecto/texturas/humano"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, -0.8, 0)
scale = (0.7, 0.7, .7)
rotate = (0, -pi/2, 0)
glIntensidadLuz(2)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 5 (mascara 1)
objeto = "models_proyecto/mask1"
textura = "models_proyecto/texturas/mask1"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, 0.4, 0.38)
scale = (1.9, 1.9, 1.9)
rotate = (0, pi/5, 0)
glIntensidadLuz(0.9)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 6 (mascara 2)
objeto = "models_proyecto/mask2"
textura = "models_proyecto/texturas/mask2"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, -0.27, -0.4)
scale = (1.5, 1.5, 1.5)
rotate = (-pi/3.5, pi/6, -pi/3.5)
glIntensidadLuz(2)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)

# objeto 7 (mascara 3)
objeto = "models_proyecto/mask3"
textura = "models_proyecto/texturas/mask3"
glLookAt((1, 0, 0), (0, 0, 0), (0, 1, 0))
glViewPort(0, 0, 1024, 1024)
glTexture(textura)
translate = (0, 2.65, -1.55)
scale = (1.5, 1.5, 1.5)
rotate = (0, pi/1.4, pi/3)
glIntensidadLuz(5)
glLoadMMatriz(translate, scale, rotate)
generar_objeto(objeto, color)


# RENDER
glFinish("escena_final")
