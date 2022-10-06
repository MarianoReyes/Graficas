from encodings import normalize_encoding
from render import *
from vector import V3
global r


def glInit():
    global r
    r = Render()


def glTexture(nombre):
    r.get_Texture(nombre+".bmp")


def glNormalMapping(nombre):
    r.get_Normatrizmapping(nombre+".bmp")


def glIntensidadLuz(num):
    r.constantLuz = num


def glPixel(coordenada, tam):
    temp = coordenada / tam
    return (temp*2)-1


def glCreateWindow(width, height):
    r.bufferStart(width, height)


def glViewPort(x, y, width, height):
    r.viewPort(x, y, width, height)


def glClear():
    r.clear()


def glClearColor(red, g, b):
    r.backgroundcolor(red, g, b)


def glVertex(x, y):
    r.point(*r.vertexConvert(x, y))


def glColor(red, g, b):
    r.pointcolor(red, g, b)


def glLine(x0, y0, x1, y1):
    r.line(*r.vertexConvert(glPixel(x0, 500), glPixel(y0, 500)),
           *r.vertexConvert(glPixel(x1, 500), glPixel(y1, 500)))


def glTriangulo(V1, V2, V3):
    r.triangle((V1, V2, V3))


def glLoadMMatriz(translate_factor, scale_factor, rotate):
    r.loadModelMatriz(translate_factor, scale_factor, rotate)


def glLookAt(eye, center, up):
    r.lookAt(eye, center, up)


def generar_objeto(nombre, color):
    r.generar_objeto(nombre, color)


def glFondo(nombre):
    r.background(nombre+".bmp")


def glFinish(nombre):
    r.write(nombre+'.bmp')
