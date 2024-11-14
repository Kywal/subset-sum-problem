def merge_lists(l: list[int], r: list[int]):
    merged_list = sorted(set(l + r))
    return merged_list