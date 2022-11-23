from Color import *


def shader_planeta(**kwargs):
    w, u, v = kwargs['bar']
    A, B, C = kwargs['vertices']
    L = kwargs['light']
    nA, nB, nC = kwargs['normals']
    y = kwargs['height']
    x = kwargs['width']

    iA = nA.normalize() @ L.normalize()
    iB = nB.normalize() @ L.normalize()
    iC = nC.normalize() @ L.normalize()

    # intensity
    i = iA * w + iB * u + iC * v
    i *= -1

    if x > 405 and x < 435:
        if y > 490 and y < 500:
            return color(clamping(197*i), clamping(137*i), clamping(74*i))
    if x > 395 and x < 445:
        if y > 480 and y < 490:
            return color(clamping(197*i), clamping(137*i), clamping(74*i))
    if x > 385 and x < 455:
        if y > 470 and y < 480:
            return color(clamping(197*i), clamping(137*i), clamping(74*i))
    if x > 375 and x < 465:
        if y > 460 and y < 470:
            return color(clamping(197*i), clamping(137*i), clamping(74*i))
    if x > 365 and x < 475:
        if y > 462 and y < 467:
            return color(clamping(197*i), clamping(137*i), clamping(74*i))
    if x > 375 and x < 465:
        if y > 450 and y < 460:
            return color(clamping(197*i), clamping(137*i), clamping(74*i))
    if x > 385 and x < 455:
        if y > 440 and y < 450:
            return color(clamping(197*i), clamping(137*i), clamping(74*i))
    if x > 395 and x < 445:
        if y > 430 and y < 440:
            return color(clamping(197*i), clamping(137*i), clamping(74*i))
    if x > 405 and x < 435:
        if y > 420 and y < 430:
            return color(clamping(197*i), clamping(137*i), clamping(74*i))

    if y > 850:
        return color(clamping(99*i), clamping(83*i), clamping(64*i))
    if y <= 850 and y > 840:
        return color(clamping(159*i), clamping(167*i), clamping(166*i))
    if y <= 840 and y > 830:
        return color(clamping(115*i), clamping(106*i), clamping(97*i))
    if y <= 830 and y > 730:
        return color(clamping(159*i), clamping(167*i), clamping(166*i))
    if y <= 730 and y > 700:
        return color(clamping(113*i), clamping(82*i), clamping(52*i))
    if y <= 700 and y > 650:
        return color(clamping(157*i), clamping(147*i), clamping(139*i))
    if y <= 650 and y > 620:
        return color(clamping(159*i), clamping(167*i), clamping(166*i))
    if y <= 620 and y > 500:
        return color(clamping(149*i), clamping(133*i), clamping(118*i))
    if y <= 500 and y > 470:
        return color(clamping(133*i), clamping(113*i), clamping(91*i))
    if y <= 470 and y > 370:
        return color(clamping(159*i), clamping(167*i), clamping(166*i))
    if y <= 370 and y > 280:
        return color(clamping(213*i), clamping(190*i), clamping(155*i))
    if y <= 280:
        return color(clamping(159*i), clamping(139*i), clamping(113*i))
