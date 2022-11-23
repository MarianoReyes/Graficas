# implementacion del shader a un objeto circular en forma de planeta
# se simula jupiter

from gl import *
from shader import *

glCreateWindow(1024, 1024)

# color de fondo igual a referencia de jupiter.jpg
glClearColor(0, 0, 0)
glClear()

glViewPort(0, 0, 1024, 1024)

glLookAt((0, 0, 100), (0, 0, 0), (0, 1, 0))

# funcion del gl creada para colocarle shader al objeto circular del planeta
# se realizo una clase separada de shader para asemejarse al trabajo con textura y un mayor orden
glShader(shader_planeta)

glRenderObject('./planeta.obj', scale=(0.0008, 0.0008, 0.0008),
               translate=(0, 0, 0), rotate=(0, 0, 0))

glFinish('lab2.bmp')
