def sum_p(x: list[int], w: list[int]):
    multiset_size = len(x)
    result = 0
    for i in range(multiset_size):
        result += x[i] * w[i]
    return result

def fitness(x: list[int], w: list[int], c: int):
    s = 0
    px = sum_p(x, w)
    if c - px >= 0:
        s = 1
    return s * (c - px) + (1 - s) * px

def difference_degree(parent_x: list[int], parent_y: list[int]):
    multiset_size = len(parent_x)
    nd = 0
    for i in range(multiset_size):
        if parent_x[i] != parent_y[i]:
            nd += 1
    ng = multiset_size
    return nd / ng

# def selection():
