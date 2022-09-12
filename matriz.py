class MatrizO(object):
    def __init__(self, matriz):
        self.matriz = matriz

    def __add__(self, other):
        try:
            for y in range(len(self.matriz)):
                for x in range(len(self.matriz[y])):
                    self.matriz[x][y] += other.matriz[x][y]
            return self.matriz

        except:
            print('Error en la suma')

    def __sub__(self, other):
        try:
            for y in range(len(self.matriz)):
                for x in range(len(self.matriz[y])):
                    self.matriz[x][y] -= other.matriz[x][y]
            return self.matriz

        except:
            print('Error en la suma')

    def __mul__(self, other):
        from vector import V4
        try:

            if(type(other) == V4):
                other = MatrizO([[other.x], [other.y], [other.z], [other.w]])

            resultado = []
            for i in range(len(self.matriz)):
                resultado.append([])
                for j in range(len(other.matriz[0])):
                    resultado[i].append([])
                    temp = 0
                    for k in range(len(other.matriz)):
                        temp += self.matriz[i][k] * other.matriz[k][j]
                    resultado[i][j] = temp
            return MatrizO(resultado)

        except:
            print('Error en la multiplicación')
