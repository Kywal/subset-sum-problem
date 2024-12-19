import time
from exact_subset_sum.src.exact_subset_sum import all_subset_sums
from cormen_approximation_scheme.src.approx_subset_sum import approx_subset_sum

def run_exact(t,s,list_o) -> dict[str, any]:
    start_time = time.perf_counter_ns()
    result = all_subset_sums(s,t)
    end_time = time.perf_counter_ns()
    data = {
        "len" : len (s),
        "t" : t,
        "set" : s,
        "final_sum": result,
        "duration": end_time - start_time,
        "duration_sec": (end_time - start_time) / 1_000_000_000,
        "config_o": list_o if list_o != [] else []
    }
    return data

def run_aprox(t,s,list_o) -> dict[str, any]:
    start_time = time.perf_counter_ns()
    result = approx_subset_sum(s,t,0.4)
    end_time = time.perf_counter_ns()
    data = {
        "len" : len (s),
        "t" : t,
        "set" : s,
        "final_sum": result[0],
        "final_config" :str(result[1]),
        "duration": end_time - start_time,
        "duration_sec": (end_time - start_time) / 1_000_000_000,
        "config_o": list_o if list_o != [] else []
    }
    return data