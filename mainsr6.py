from render import Render

r = Render()

r.bufferStart(1000, 1000)

r.backgroundcolor(1, 1, 1)
r.clear()
r.color_pixel(1, 1, 1)

r.get_Texture('models/texturas/txt-dado-2.bmp')

color = (0, 0, 0)

scale_factor = (1, 1, 1)
translate_factor = (0, 0, 0)
rotate = (0, 0, 0)

# toma medium
r.lookAt((0, 0, 0.2), (0, 0, 0), (0, 0.1, 0))
r.generar_3d('models/Dice.obj', scale_factor, translate_factor, rotate)
r.write('dado_mediumView.bmp')
'''
# toma low
r.lookAt((0, -8, 10), (0, 0, 0), (0, 1, 0))
r.generar_3d('models/Dice.obj', scale_factor, translate_factor, color)
r.write('dado_lowView.bmp')
# toma high
r.lookAt((0, 9, 10), (0, 0, 0), (0, 1, 0))
r.generar_3d('models/Dice.obj', scale_factor, translate_factor, color)
r.write('dado_highView.bmp')
# toma dutch
r.lookAt((1, 0, 2), (0, 0.1, 0.3), (-0.9, 1, 0))
r.generar_3d('models/Dice.obj', scale_factor, translate_factor, color)
r.write('dado_dutchView.bmp')
'''
