# -*- coding: utf8 -*-
"""
Zakladni sablona pro prvni cviceni
"""

#test
"""
#False
a = 4
b = 5
c = 12
"""
#True
a = 3
b = 4
c = 5

"""
Funkce vrací True nebo False, podle toho zda strany a, b, c mohou tvořit
pravoúhlý trojúhelník

Pro jednoduchost můžete předpokládat, že strany a, b jsou odvěsny, c je přepona. 
Tak jako je to ve známé matematické poučce. 
"""

def triangle(a, b, c):
    if (c**2 == a**2 + b**2) and (a and b and c > 0):
        return True
    else:
        return False

print(triangle(a, b, c))
