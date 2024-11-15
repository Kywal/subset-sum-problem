from merge_lists import merge_lists
from trim import trim


def approx_subset_sum(s: list[int], t: int, e: float):
    n = len(s)
    lists = [[0]] + [[] for i in range(n)]

    is_less_or_equal_than_t = lambda a : True if a <= t else False
    print("---------------")
    for i in range(1, n+1): 
        sum_si = lambda a : a + s[i-1]

        lists[i] = merge_lists(
            lists[i-1], list(map(sum_si,lists[i-1])
            )
        )

        print ("pre-trim: " , lists[i])
        
        lists[i] = trim(lists[i], e/(2*n))
        lists[i] = list(
            filter(is_less_or_equal_than_t,lists[i])
        )
        print ("L", i , ": " , lists[i])

    return max(lists[n]) if lists[n] else 0



