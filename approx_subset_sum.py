
def approx_subset_sum(s: list[int], t: int, e: float):
    n = len(s)
    lists = [[0]]*n
    for i in range(1, n-1):
        lists[i] = merge_lists(lists[i-1], sum_num_list(lists[i-1], s[i]))
        lists[i] = trim(lists[i], e/2*n)
        lists[i] = rm_bigger_than(lists[i], t)

    return max(lists[n-1])


def sum_num_list(l: list[int], n: int):
    for i in range(0, len(l)):
        l[i] += n
    return l

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


def rm_bigger_than(l: list[int], v: int):
    for i in range(0, len(l)):
        if l[i] > v:
            l.pop(i)

    return l


