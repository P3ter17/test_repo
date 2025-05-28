import math as m

def calculate_triangle_angles(a, b, c):
    if a and b and c > 0:
        alfa = (c**2+b**2-a**2)/(2*b*c)
        beta = (a**2+c**2-b**2)/(2*a*b)
        gama = (a**2+b**2-c**2)/(2*a*b)
        alfa = round(m.degrees(m.acos(alfa)), 2)
        beta = round(m.degrees(m.acos(beta)), 2)
        gama = round(m.degrees(m.acos(gama)), 2)
        return alfa, beta, gama
    else:
        return None, None, None





