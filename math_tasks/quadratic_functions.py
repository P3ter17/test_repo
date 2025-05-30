import math as m
def root_of_quadratic_fun(a, b, c):
    discriminant = b**2 - 4*a*c
    if a != 0:
        if discriminant < 0:
            return None, None
        elif discriminant == 0:
            x = -b / (2*a)
            return x, None
        else:
            x1 = (-b + m.sqrt(discriminant)) / (2*a)
            x2 = (-b - m.sqrt(discriminant)) / (2*a)
            return x1, x2
    else:
        return None, None
