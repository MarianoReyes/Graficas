class MM(object):
    def __init__(self, matriz):
        self.matriz = matriz

    def __mul__(self, other):

        selfy = len(self.matriz)
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
        return MM(Multiplicacion)

    def __add__(self, other):
        try:
            suma = [[0 for y in range(len(self.matriz))]
                    for x in range(len(self.matriz))]
            for y in range(len(self.matriz)):
                for x in range(len(self.matriz[0])):
                    suma[y][x] = self.matriz[y][x]+other.matriz[y][x]

            return MM(suma)
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
