import sys

def merge_lists(l: list[(int, list[int])], r: list[(int, list[int])]):
    merged_list = []

    n = len(l) + len(r)

    p = 0
    q = 0

    l.append((sys.maxsize, []))
    r.append((sys.maxsize, []))

    for i in range(0, n):
        if l[p][0] <= r[q][0]:
            merged_list.append(l[p])
            p += 1
        else:
            merged_list.append(r[q])
            q += 1

    return merged_list


    # O endereço após o último endereço de uma das listas vai necessariamente ser acessado
    # Então, para que um endereço inválido não seja acessado cada um deles recebe "+infinito"
    # E esse endereço não pode fazer parte da merged_list