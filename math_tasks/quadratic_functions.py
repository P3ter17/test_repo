def root_of_quadratic_fun(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        x = -b / (2*a)
        return x, None
    else:
        x1 = (-b + discriminant) / (2*a)
        x2 = (-b - discriminant) / (2*a)
        return x1, x2