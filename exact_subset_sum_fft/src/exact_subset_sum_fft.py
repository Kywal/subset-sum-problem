import math
from collections import defaultdict
from exact_subset_sum_fft.src.pairwise import pairwise_u_ari2, pairwise_u_fft

def all_subset_sums_fft(S: list[int], u: int):
    n = len(S)
    b = int(math.sqrt(n * math.log(n)))
    subsets_by_mod = defaultdict(list)  # auxiliar
    
    for x in S:
        subsets_by_mod[x % b].append(x)

    results = []
    for l in range(b):
        S_l = subsets_by_mod[l]
        Q_l = [(x - l) // b for x in S_l]
        S_card = all_subset_sums_card(Q_l, u // b)
        R_l = [(z * b + l * j) for (z, j) in S_card if z * b + l * j <= u] # for ali para capturar o conjunto gerador, acho que aumentou o custo do role ein
        if len(R_l) != 0:
            results.append(R_l)

    final_result = results[0]
    for r in results[1:]:
        final_result = pairwise_u_fft(final_result, r, u)
    return (max(final_result),[]) 


def all_subset_sums_card(S: list[int], u: int):
    if len(S) == 1:
        x = S[0]
        return [(0, 0), (x, 1)]  
    elif len(S) == 0:
        return [(0, 0)]  

    T = S[:len(S) // 2]

    left = all_subset_sums_card(T, u)
    right = all_subset_sums_card(S[len(T):], u)

    return pairwise_u_ari2(left, right, u)


