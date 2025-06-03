import math as m

def calculate_triangle_angles(a, b, c):
    if a > 0 and b >0 and c > 0:
        biggest_side = max(a, b, c)
        small_mid = (a + b + c) - biggest_side
        if small_mid > biggest_side:
            alfa = (c**2+b**2-a**2)/(2*b*c)
            beta = (a**2+c**2-b**2)/(2*a*c)
            gama = (a**2+b**2-c**2)/(2*a*b)
            alfa = round(m.degrees(m.acos(alfa)), 2)
            beta = round(m.degrees(m.acos(beta)), 2)
            gama = round(m.degrees(m.acos(gama)), 2)
            return alfa, beta, gama
        else:
            return None, None, None
    else:
        return None, None, None




