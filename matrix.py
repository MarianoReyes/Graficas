class matrizO(object):
    def __init__(self, matriz):
        self.matriz = matriz

    def __matmul__(self, other):

        selfy = len(self.matriz)
        selfx = len(self.matriz[0])

        othery = len(other.matriz)
        otherx = len(other.matriz[0])

        Multiplicacion = []

        for i in range(selfy):
            Multiplicacion.append([])
            for j in range(otherx):
                Multiplicacion[i].append([])
                temp = 0
                for k in range(othery):
                    temp += self.matriz[i][k]*other.matriz[k][j]
                Multiplicacion[i][j] = temp
        return matrizO(Multiplicacion)

    def __mul__(self, other):
        selfy = len(self.matriz)

        othery = len(other.matriz)
        otherx = len(other.matriz[0])

        if(otherx == 1):
            Multiplicacion = [[self.matriz[0][0] * other.matriz[0][0] + self.matriz[0][1] * other.matriz[1][0]+self.matriz[0][2] * other.matriz[2][0]+self.matriz[0][3] * other.matriz[3][0]],
                              [self.matriz[1][0] * other.matriz[0][0] + self.matriz[1][1] * other.matriz[1][0] +
                                  self.matriz[1][2] * other.matriz[2][0]+self.matriz[1][3] * other.matriz[3][0]],
                              [self.matriz[2][0] * other.matriz[0][0] + self.matriz[2][1] * other.matriz[1][0] +
                                  self.matriz[2][2] * other.matriz[2][0]+self.matriz[2][3] * other.matriz[3][0]],
                              [self.matriz[3][0] * other.matriz[0][0] + self.matriz[3][1] * other.matriz[1][0] +
                                  self.matriz[3][2] * other.matriz[2][0]+self.matriz[3][3] * other.matriz[3][0]]
                              ]
            return matrizO(Multiplicacion)
        else:
            Multiplicacion = []

            for i in range(selfy):
                Multiplicacion.append([])
                for j in range(otherx):
                    Multiplicacion[i].append([])
                    temp = 0
                    for k in range(othery):
                        temp += self.matriz[i][k]*other.matriz[k][j]
                    Multiplicacion[i][j] = temp
            return matrizO(Multiplicacion)

    def __add__(self, other):
        try:
            suma = [[0 for y in range(len(self.matriz))]
                    for x in range(len(self.matriz))]
            for y in range(len(self.matriz)):
                for x in range(len(self.matriz[0])):
                    suma[y][x] = self.matriz[y][x]+other.matriz[y][x]

            return matrizO(suma)
        except:
            print("ERROR SUMA INVALIDAD")

    def __repr__(self):
        a = ""
        for y in range(len(self.matriz)):
            a += "["
            for x in range(len(self.matriz[0])):
                a += str(self.matriz[y][x])+","
            a = a[0:len(a)-1]
            a += "]\n"
        return a
