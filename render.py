from obj import Obj
from writeutilities import *
from color import *
from vector import V3
from textures import *
from math import *
from matriz import MM


class Render(object):

    def __init__(self, width=None, height=None):
        self.color_pixel(1, 0, 1)
        self.yVp = 0
        self.xVp = 0
        self.width = width
        self.height = height
        self.texture = None

    def vertexConvert(self, x, y):
        return [round(self.xVp+(x+1)*0.5*self.widthVp-1), round(self.yVp+(y+1)*0.5*self.heightVp-1)]

    def viewPort(self, x, y, neww, newh):
        self.widthVp = neww
        self.heightVp = newh
        self.yVp = y
        self.xVp = x

    def get_Texture(self, nombre):
        t = Texture(nombre)
        self.texture = t

    def backgroundcolor(self, r, g, b):
        self.color = [intcolor(r), intcolor(g), intcolor(b)]

    def color_pixel(self, r, g, b):
        #print("red:"+str(r)+" green: "+str(g)+" blue: "+str(b))
        self.pcolor = [intcolor(r), intcolor(g), intcolor(b)]

    def bufferStart(self, width, height):
        self.width = width
        self.height = height
        self.heightVp = height
        self.widthVp = width

        self.backgroundcolor(0, 0, 0)
        self.clear()

    def clear(self):
        self.framebuffer = [
            [color(*self.color) for x in range(self.width)]
            for y in range(self.height)
        ]

        self.zBuffer = [
            [-99999 for x in range(self.width)]
            for y in range(self.height)
        ]

        self.zpaint = [
            [color(*(10, 50, 180)) for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename="a.bmp"):
        f = open(filename, 'bw')

        extraBytes = (4 - (self.width * 3) % 4) % 4
        new_width_bytes = (self.width * 3) + extraBytes

        # pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + new_width_bytes * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))

        # info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.height * self.width * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data

        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
            extra = []
            for i in range(extraBytes):
                extra.append(0)
            f.write(bytes(extra))
        f.close()
        # self.writez()

    def writez(self):
        f = open("zbuffer.bmp", 'bw')

        extraBytes = (4 - (self.width * 3) % 4) % 4
        new_width_bytes = (self.width * 3) + extraBytes

        # pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + new_width_bytes * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))

        # info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.height * self.width * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data

        for x in range(self.height):
            for y in range(self.width):
                f.write(self.zpaint[x][y])
            extra = []
            for i in range(extraBytes):
                extra.append(0)
            f.write(bytes(extra))
        f.close()

    def point(self, x, y):
        if (x < self.width and x >= 0 and y < self.height and y >= 0):
            self.framebuffer[y][x] = color(*self.pcolor)

    def bounding_box(self, A, B, C):
        xs = [A.x, B.x, C.x]
        ys = [A.y, B.y, C.y]

        xs.sort()
        ys.sort()
        return V3(xs[0], ys[0]), V3(xs[-1], ys[-1])

    def baricentric(self, A, B, C, P):
        cx, cy, cz = V3.cross(
            V3(B.x - A.x, C.x - A.x, A.x - P.x),
            V3(B.y - A.y, C.y - A.y, A.y - P.y)
        )

        u = cx / cz
        v = cy / cz
        w = 1 - (cx + cy)/cz
        return (w, v, u)

    def loadModelMatriz(self, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
        translate = V3(*translate)
        scale = V3(*scale)
        rotate = V3(*rotate)

        translateM = MM([
            [1, 0, 0, translate.x],
            [0, 1, 0, translate.y],
            [0, 0, 1, translate.z],
            [0, 0, 0, 1]
        ])

        scaleM = MM([
            [scale.x,      0,      0, 0],
            [0, scale.y,      0, 0],
            [0,      0, scale.z, 0],
            [0,      0,      0, 1]
        ])
        a = rotate.x
        rotacionx = MM([
            [1,     0,           0, 0],
            [0, cos(a),    -sin(a), 0],
            [0, sin(a),     cos(a), 0],
            [0,     0,          0,  1]
        ])
        a = rotate.y
        rotaciony = MM([
            [cos(a),     0,    sin(a), 0],
            [0,     1,         0, 0],
            [-sin(a),     0,    cos(a), 0],
            [0,     0,         0, 1]
        ])
        a = rotate.z
        rotacionz = MM([
            [cos(a), -sin(a),    0, 0],
            [sin(a), cos(a),    0, 0],
            [0,      0,    1, 0],
            [0,      0,    0, 1]
        ])
        rotacionM = rotacionx * rotaciony * rotacionz
        self.Model = translateM * rotacionM * scaleM

    def triangle(self, Vertices, Tvertices=None):

        if self.texture:
            tA, tB, tC = Tvertices
        v1, v2, v3 = Vertices
        L = V3(0, 0, -1)
        N = (v3-v1) * (v2-v1)
        i = N.norm() @ L.norm()

        if i <= 0 or i > 1:
            return

        if not self.texture:
            self.pcolor = (
                round(self.pcolor[0]*i), round(self.pcolor[1]*i), round(self.pcolor[2]*i))

        Bmin, Bmax = self.bounding_box(v1, v2, v3)
        Bmin.round()
        Bmax.round()

        for x in range(Bmin.x, Bmax.x+1):
            for y in range(Bmin.y, Bmax.y+1):
                w, v, u = self.baricentric(v1, v2, v3, V3(x, y))

                if(w < 0 or v < 0 or u < 0):
                    continue

                z = v1.z * w + v2.z * v + v3.z * u
                if (self.zBuffer[x][y] < z):
                    self.zBuffer[x][y] = z

                    if self.texture:
                        tx = tA.x * w + tB.x * u + tC.x * v
                        ty = tA.y * w + tB.y * u + tC.y * v
                        self.pcolor = self.texture.intensity(tx, ty, i)
                    # if self.pcolor:
                    self.point(x, y)
        pass

    def clamp(self, val):
        temp = round(val*255)
        return max(0, min(temp, 255))

    def line(self, V1, V2):
        x0 = V1.x
        y0 = V1.y
        x1 = V2.x
        y1 = V2.y
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        threshold = dx * 2
        y = y0
        for x in range(x0, x1+1):
            if steep:
                self.point(y, x)

            else:
                self.point(x, y)

            offset += dy*2
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += dx*2

    def transform_vertex(self, vertex, scale, translate):
        if len(vertex) == 2:
            vertex.append(0)
        return V3(
            round(vertex[0] * scale[0] + translate[0]),
            round(vertex[1] * scale[1] + translate[1]),
            round(vertex[2] * scale[2] + translate[2])
        )

    def generar_3d(self, nombre, scale_factor, translate_factor, color):
        model = Obj(nombre)

        for face in model.caras:
            face.pop()

            self.color_pixel(*color)

            if len(face) == 3:

                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1

                v1 = self.transform_vertex(
                    model.vertices[face[0][0] - 1], scale_factor, translate_factor)
                v2 = self.transform_vertex(
                    model.vertices[face[1][0] - 1], scale_factor, translate_factor)
                v3 = self.transform_vertex(
                    model.vertices[face[2][0] - 1], scale_factor, translate_factor)

                if self.texture and len(model.tvertices) != 0:

                    ft1 = face[0][1] - 1
                    ft2 = face[1][1] - 1
                    ft3 = face[2][1] - 1

                    vt1 = V3(*model.tvertices[ft1])
                    vt2 = V3(*model.tvertices[ft2])
                    vt3 = V3(*model.tvertices[ft3])

                    self.triangle((v1, v2, v3), (vt1, vt2, vt3))

                else:
                    self.triangle((v1, v2, v3))

            if len(face) == 4:

                # assuming 4
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1
                f4 = face[3][0] - 1

                vertices = [
                    self.transform_vertex(
                        model.vertices[f1], scale_factor, translate_factor),
                    self.transform_vertex(
                        model.vertices[f2], scale_factor, translate_factor),
                    self.transform_vertex(
                        model.vertices[f3], scale_factor, translate_factor),
                    self.transform_vertex(
                        model.vertices[f4], scale_factor, translate_factor)
                ]

                if self.texture and len(model.tvertices) != 0:

                    ft1 = face[0][1] - 1
                    ft2 = face[1][1] - 1
                    ft3 = face[2][1] - 1
                    ft4 = face[3][1] - 1

                    vt1 = V3(*model.tvertices[ft1])
                    vt2 = V3(*model.tvertices[ft2])
                    vt3 = V3(*model.tvertices[ft3])
                    vt4 = V3(*model.tvertices[ft4])

                    A, B, C, D = vertices
                    self.triangle((A, B, C), (vt1, vt2, vt3))
                    self.triangle((A, C, D), (vt1, vt3, vt4))

                else:
                    A, B, C, D = vertices

                    self.triangle((A, B, C))
                    self.triangle((A, C, D))
