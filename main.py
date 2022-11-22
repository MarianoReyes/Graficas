from gl import *

fondo = "espacio"
objeto = "planeta"
glInit()
glCreateWindow(720, 720)
glViewPort(0, 0, 720, 720)
glClearColor(0, 0, 0)
glClear()
glColor(1, 1, 1)
color = (1, 0, 1)
# glTexture(objeto)
glFondo(fondo)
translate_factor = (0, 0, 0)
scale_factor = (0.65, 0.65, 0.65)
rotate = (0, 0, 0)
glLoadMMatriz(translate_factor, scale_factor, rotate)
# En cámara ingresar el tipo de toma que se desea ver
# Se dibujara en R2-D23D
camara = "medium"
glCamaraVista(camara)
obj3D(objeto, color)
glFinish(objeto+"3D")


# glPlano(objeto,objeto,4096,4096)
