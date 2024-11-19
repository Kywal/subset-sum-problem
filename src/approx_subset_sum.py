from merge_lists import merge_lists
from trim import trim


def approx_subset_sum(s: list[int], t: int, e: float):
    n = len(s)
    lists = [[(0, [])]] + [[] for _ in range(n)] # as tuplas aqui eh pra conseguir armazenar a configuracao que deu a soma

    is_less_or_equal_than_t = lambda a : True if a[0] <= t else False 
    for i in range(1, n+1): 
        sum_si = lambda a : (a[0] + s[i - 1], a[1] + [s[i - 1]]) 

        lists[i] = merge_lists(
            lists[i-1], list(map(sum_si,lists[i-1])
            )
        )
        
        lists[i] = trim(lists[i], e/(2*n))
        lists[i] = list(
            filter(is_less_or_equal_than_t,lists[i])
        )
        print ("L", i , ": " , lists[i])

    max_tuple = max(lists[n], key=lambda x: x[0]) if lists[n] else (0, [])
    print(max_tuple)
    
    return max_tuple[0]



