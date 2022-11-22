def rgbcolor(r, g, b):
    b = max(0, min(b, 255))
    g = max(0, min(g, 255))
    r = max(0, min(r, 255))

    return bytes([b, g, r])


def color_clamping(r, g, b):
    return rgbcolor(clamping(r*255), clamping(g*255), clamping(b*255))


def clamping(num):
    return int(max(min(num, 255), 0))
