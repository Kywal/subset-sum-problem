import time
from exact_subset_sum_simple.src.exact_subset_sum_simple import all_subset_sums_simple
from exact_subset_sum_fft.src.exact_subset_sum_fft import all_subset_sums_fft
from exact_subset_sum_mp.src.exact_subset_sum_mp import all_subset_sums_mp
from cormen_approximation_scheme.src.approx_subset_sum import approx_subset_sum

def run_exact_fft(t,s,list_o) -> dict[str, any]:
    start_time = time.perf_counter_ns()
    result = all_subset_sums_fft(s, t)
    end_time = time.perf_counter_ns()
    data = {
        "len" : len (s),
        "t" : t,
        "set" : s,
        "final_sum": result[0],
        "final_config": result[1],
        "duration": end_time - start_time,
        "duration_sec": (end_time - start_time) / 1_000_000_000,
        "config_o": list_o if list_o != [] else []
    }
    return data

def run_exact_simple(t,s,list_o) -> dict[str, any]:
    start_time = time.perf_counter_ns()
    result = all_subset_sums_simple(s, t)
    end_time = time.perf_counter_ns()
    data = {
        "len" : len (s),
        "t" : t,
        "set" : s,
        "final_sum": result[0],
        "final_config": result[1],
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


def run_exact_mp(t,s,list_o) -> dict[str, any]:
    start_time = time.perf_counter_ns()
    result = all_subset_sums_mp(s, t)
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