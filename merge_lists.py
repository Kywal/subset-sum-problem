def merge_lists(l, r):
    merged_list = l+r
    merged_list.sort(key=lambda x: x[0])
    return merged_list