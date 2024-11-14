def merge_lists(l: list[int], r: list[int]):
    final_list = []

    n = 0
    l_size = len(l)
    r_size = len(r)
    if l_size >= r_size:
        n = l_size
    else:
        n = r_size

    p = 0
    q = 0

    for i in range(0,n):
        if p < l_size and q < r_size:
            if l[p] <= r[q]:
                final_list.append(l[p])
                p += 1
            else:
                final_list.append(r[q])
                q += 1

    return final_list