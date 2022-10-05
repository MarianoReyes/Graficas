
def rgbcolor(r, g, b):
    return bytes([b, g, r])


def intcolor(n):
    return round(n*255)


def intcolora(n):
    return [round(n[0]*255), round(n[1]*255), round(n[2]*255)]
