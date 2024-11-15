def trim(l:  list[tuple[int, list[int]]], e: float):
    l2 = []

    if len(l) >= 1:
        last = l[0][0]
        l2 = [l[0]]

        for i in range(1, len(l)):
            if float(l[i][0]) > last * (1 + e):
                l2.append(l[i])
            last = l[i][0]

    return l2