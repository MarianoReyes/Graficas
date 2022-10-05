from gl import *
from math import pi

objeto = "models/Mask"
textura = "models/texturas/mask"

glInit()
glCreateWindow(480, 480)
glViewPort(0, 0, 1024, 1024)
glClearColor(1, 1, 1)
glClear()
glColor(1, 1, 1)
color = (0, 0, 1)

glTexture(textura)

translate_factor = (0, 0, 0)
scale_factor = (5, 5, 5)
rotate = (0, pi/4, 0)

glLoadMMatriz(translate_factor, scale_factor, rotate)

# TIPOS DE CAMARA
# medium
""" camara = "medium"
glCamaraVista(camara)
generar_objeto(objeto, color)
glFinish("mask_medium") """

# high
""" camara = "high"
glCamaraVista(camara)
generar_objeto(objeto, color)
glFinish("mask_high") """

# low
""" camara = "low"
glCamaraVista(camara)
generar_objeto(objeto, color)
glFinish("mask_low") """

# dutch
camara = "dutch"
glCamaraVista(camara)
generar_objeto(objeto, color)
glFinish("mask_dutch")
