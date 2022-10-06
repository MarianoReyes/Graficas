class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()

        self.vertices = []
        self.caras = []
        self.tvertices = []
        self.body = []
        self.nvertices = []

        for line in self.lines:
            if (line != "" and len(line.split(' ', 1)) > 1):
                prefix, value = line.split(' ', 1)
            if prefix == 'v':
                self.vertices.append(
                    list(
                        map(float, value.split(' '))
                    )
                )
            if prefix == 'vt':
                self.tvertices.append(
                    list(
                        map(float, value.split(' '))
                    )
                )

            if prefix == 'f':
                self.caras.append([
                    list(map(int, face.split('/')))
                    for face in value.split(' ')
                ])

            if prefix == 'vn':
                self.nvertices.append(
                    list(
                        map(float, value.split(' '))
                    )
                )
