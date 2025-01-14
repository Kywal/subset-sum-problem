def multiply_polynomials(poly1, poly2):
    result_size = len(poly1) + len(poly2) - 1
    result = [0] * result_size
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]

    return result