from render import Render
from math import *

r = Render()

r.bufferStart(1000, 1000)

r.backgroundcolor(1, 1, 1)
r.clear()
r.color_pixel(1, 1, 1)

r.get_Texture('models/texturas/txt-dado-3.bmp')

color = (0, 0, 0)
scale_factor = (2, 2, 2)
translate_factor = (500, 500, 500)

#r.generar_3d('models/face', scale_factor, translate_factor, color)
rotate = (0, -pi/3, 0)
r.loadModelMatriz(translate_factor, scale_factor, rotate)
r.generar_3d('models/Dice.obj', color)

r.write('dado.bmp')
