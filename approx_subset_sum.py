
def approx_subset_sum(s: list, t: int, e: float):
    n = len(s)
    lists = [[0],[]]
    for i in range(1, n):
        lists[i] = merge_lists(lists[i-1], sum_num_list(lists[i], s[i]))
        lists[i] = trim(lists[i], e/2*n)
        lists[i] = rm_bigger_than(s[i], t)

    return max(lists[n])


def sum_num_list(l: list, n: int):
    for i in range(0, len(l)):
        l[i] += n
    return l

def merge_lists(l: list, r: list):
    final_list = []

    n = 0
    l_size = len(l)
    r_size = len(r)
    if l_size >= r_size:
        n = len(l)
    else:
        n = r_size

    p = 0
    q = 0

    for i in range(0,n):
        if l[p] <= r[q]:
            final_list.append(l[p])
            p += 1
        else:
            final_list.append(r[q])
            q += 1

    return final_list

def trim(l: list, e: float):
    last = l[0]
    l2: list = [last]

    for i in range(1, len(l)):
        if l[i] > last * (1 + e):
            l2.append(l[i])
        last = l[i]

    return l2


def rm_bigger_than(l: list, v: int):
    for i in l:
        if i > v:
            l.remove(i)

    return l


