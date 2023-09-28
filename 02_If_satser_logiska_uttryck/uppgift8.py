import math

radie = float(input("Ange cirkelns radie: "))
omkrets = 2 * math.pi * radie
if omkrets > 50:
    print("Stor cirkel.")
else:
    print("Liten cirkel.")
