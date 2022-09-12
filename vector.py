from matriz import MatrizO


class V3(object):
    # creacion del vector en 3D
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    # suma de vectores
    def __add__(self, other):
        return V3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    # resta de vectores
    def __sub__(self, other):
        return V3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def round(self):
        self.x = round(self.x)
        self.y = round(self.y)
        self.z = round(self.z)

    # multiplicacion
    def __mul__(self, other):
        # se verifica si es un escalar
        if(type(other) == int or type(other) == float):
            return V3(
                self.x * other,
                self.y * other,
                self.z * other
            )
        # si es vector retorna el producto cruz
        else:
            return V3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x,
            )

    def cross(V1, V2):
        return (
            V1.y * V2.z - V1.z * V2.y,
            V1.z * V2.x - V1.x * V2.z,
            V1.x * V2.y - V1.y * V2.x,
        )

    # producto punto
    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # magnitud de un vector
    def length(self):
        return (self.x**2+self.y**2+self.z**2)**0.5

    def norm(self):
        if self.length() == 0:
            return V3(0, 0, 0)
        return self * (1/self.length())

    # coversion de matrizes
    def convert(self):
        return MatrizO([self.x, self.y, self.z])

    # print bonito
    def __repr__(self):
        return "V3(%s,%s,%s)" % (self.x, self.y, self.z)


class V4(object):
    def __init__(self, x, y, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
