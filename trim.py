def trim(l: list[int], e: float):
    l2 = []

    if len(l) >= 1:
        last = l[0]
        l2 = [last]

        for i in range(1, len(l)):
            if float(l[i]) > last * (1 + e):
                l2.append(l[i])
            last = l[i]

    return l2