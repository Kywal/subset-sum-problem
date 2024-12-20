import math

import math
import cmath

def fft(poly, invert):
    n = len(poly)
    if n == 1:
        return poly

    theta = -2 * math.pi / n if not invert else 2 * math.pi / n
    w = [complex(math.cos(theta * i), math.sin(theta * i)) for i in range(n)]
    
    p_even = poly[0::2]
    p_odd  = poly[1::2]

    poly_even = fft(p_even, invert)
    poly_odd = fft(p_odd, invert)

    Y = [0] * n
    middle = n // 2

    for k in range(n // 2):
        w_yodd_k = w[k] * poly_odd[k]
        yeven_k = poly_even[k]

        Y[k] = yeven_k + w_yodd_k
        Y[k + middle] = yeven_k - w_yodd_k

        if invert:
            Y[k] /= 2
            Y[k + middle] /= 2

    return Y



def multiply_polynomials(poly1, poly2):
    n = 1
    while n < len(poly1) + len(poly2):
        n *= 2

    ft = poly1 + [0] * (n - len(poly1))
    fs = poly2 + [0] * (n - len(poly2))

    ft = fft(ft, False)
    fs = fft(fs, False)

    g = [0]*n
    for i in range(n):
       g[i] = ft[i] * fs[i]

    result = fft(g, True)
    return [round(result[i].real) for i in range(len(result))]

    