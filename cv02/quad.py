from math import atan2,degrees
#!/bin/env python
# -*- coding: utf-8 -*-
"""
PJP - cvičení číslo 2
"""
import math

#vytvoří list úhlů
def make_angle_list(vectorList):
    angleList = []
    for i in range(0, 4):
        a = i
        b = (i + 1) % 4
        B = math.atan2(vectorList[b][1], vectorList[b][0])
        A = math.atan2(vectorList[a][1], vectorList[a][0])
        angle = B-A
        angle = degrees(angle)

        #převede záporný úhel na kladný
        if(angle < 0):
            angle = angle % 360

        angleList.append(angle)
    return angleList

#vytvoří list vektorů
def make_vector_list(pointList):
    vectorList = []
    for i in range(0, 4):
        a = i
        b = (i + 1) % 4
        vector = ((pointList[b][0] - pointList[a][0]), (pointList[b][1] - pointList[a][1]))
        vectorList.append(vector)
    return vectorList

#vytvoří list bodů
def make_point_list(a, b, c, d):
    pointList = []
    pointList.append(a)
    pointList.append(b)
    pointList.append(c)
    pointList.append(d)
    return pointList


def is_convex(a, b, c, d):
    """
    Druhým úkolem je vytvořit funkci, která ze čtyř zadaných bodů určí, 
    zda tvoří konvexní čtyřúhelník.
    
    Body na vstupu jsou zadávány jako tuple (x, y) kde x a y mohou být
    libovolná reálná čísla, tedy i záporná. Body mohou vytvořit čtyřúhelník,
    ale není to pravidlem.

    Je potřeba aby funkce hlídala i extrémní situace, jako například,
    že body čtyřúhelník vůbec nevytváří. 
    """
    pointList = make_point_list(a, b, c, d)
    vectorList = make_vector_list(pointList)
    angleList = make_angle_list(vectorList)

    #hlídá kolik úhlů je pod 90°
    for a in angleList:
        bow = 0
        if a < 90:
            bow = bow + 1

    #pokud čtyřuhelník má všechny úhly pod 90° tak vzniká tzv. motýlek a tím pádem není konvexní
    #pokud má čtyřuhelník alespoň jeden úhel větší než 180 také nemůže být konvexní
    #pokud má čtyřuhelník alespoň jeden úhel 0° nemůže být konvexní = netvoří čtyřuhelník vůbec (přímka,trojuhelník)
    for a in angleList:
        if bow == 4:
            return False
        elif a > 180:
            return False
        elif a == 0:
            return False
    return True


if __name__ == '__main__':
    print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)))    #True

    print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)))    #True
    print(is_convex((-1.0, -1.0), (1.0, -1.0), (1.0, 1.0), (-1.0, 1.0))) #True
    print(is_convex((0.0, 0.0), (1.1, 0.1), (0.9, 0.8), (0.1, 0.9)))    #True
    print(is_convex((0.0, 0.0), (1.0, 0.0), (0.3, 0.3), (0.0, 1.0)))    #False
    print(is_convex((0.0, 0.0), (0.2, 0.7), (1.0, 1.0), (0.0, 1.0)))    #False
    print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.7, 0.3)))    #False
    print(is_convex((0.7, 0.8), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)))    #False
    print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 0.0)))    #False
    print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 0.0), (0.0, 0.0)))    #False
    print(is_convex((1.0, 0.0), (1.0, 0.0), (1.0, 0.0), (1.0, 0.0)))    #False

