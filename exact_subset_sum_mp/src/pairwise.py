from exact_subset_sum_mp.src.multiply_polynomials import multiply_polynomials

def pairwise_u_ari2(X: list, Y: list, u: int):
    result = []
    for (x1, x2) in X:
        for (y1, y2) in Y:
            if x1 + y1 <= u:
                result.append((x1 + y1, x2 + y2))  
    return result


def pairwise_u_mp(X: list, Y: list, u: int):
    result = []

    n = max(X) + max(Y) + 1
    if n > u:
        n = u

    poly_X = [0] * (n + 1)
    poly_Y = [0] * (n + 1)
    
    for x1 in X:
        poly_X[x1] = 1
    for y1 in Y:
        poly_Y[y1] = 1

    result_values = multiply_polynomials(poly_X, poly_Y)

    result = [i for i in range(min(n + 1, u + 1)) if result_values[i] > 0]

    return result
