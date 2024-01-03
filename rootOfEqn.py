# mathematically we can determine the nature of the roots based on the
# discriminant .

# discriminant = b * b - 4 * a * c

# discriminant = D

# edge cases:

# D > 0 : roots are real
# D < 0 : roots are imaginary
# D = 0 : roots are real and single roots(repeated twice)


# Above is mathematical explanation , code starts here ...........................

import math


def find_roots(a, b, c):
    if a != 0:
        discriminant = b * b - 4 * a * c
        sqrt_discriminant = math.sqrt(abs(discriminant))

        if discriminant > 0:
            root_1 = (-b + sqrt_discriminant)/(2 * a)
            root_2 = (-b - sqrt_discriminant)/(2 * a)

        elif discriminant == 0:
            root_1 = root_2 = -b / (2 * a)

        else:
            root_1 = -b / (2 * a) + (sqrt_discriminant)/(2 * a) * 1j
            root_2 = -b / (2 * a) - (sqrt_discriminant)/(2 * a) * 1j

        return (root_1, root_2)
    else:
        return "coefficient of second degree should be greater than 0"

a = 2
b = 10
c = 8

roots = find_roots(a, b, c)

print(roots)
