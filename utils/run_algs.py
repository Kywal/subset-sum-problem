import time
from exact_subset_sum.exact_subset_sum_simple.src.exact_subset_sum_simple import all_subset_sums_simple
from exact_subset_sum.exact_subset_sum_fft.src.exact_subset_sum_fft import all_subset_sums_fft
from exact_subset_sum.exact_subset_sum_mp.src.exact_subset_sum_mp import all_subset_sums_mp
from cormen_approximation_scheme.src.approx_subset_sum import approx_subset_sum
from meta_heuristics_subset_sum.genetic_subset_sum.src.genetic_subset_sum import genetic_subset_sum

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

def run_genetic(t,s,list_o) -> dict[str, any]:
    start_time = time.perf_counter_ns()
    result = genetic_subset_sum(s, t, 20, 100, 0.6)
    end_time = time.perf_counter_ns()
    
    final_subset = [s[i] for i in range(len(result[0])) if result[0][i] == 1]
    print(final_subset)
    
    data = {
        "len" : len (s),
        "t" : t,
        "set" : s,
        "final_sum":  sum(final_subset),
        "final_config": str(final_subset),
        "duration": end_time - start_time,
        "duration_sec": (end_time - start_time) / 1_000_000_000,
        "config_o": list_o if list_o != [] else []
    }
    return data

def run_genetic_many_timnes(t,s,list_o) -> dict[str,any]:
    import time

def run_genetic_many_times(t, s, list_o) -> dict:
    num_runs = 30
    best_solution = None
    best_value = 0 
    sum_solutions = 0
    find_solution = 0
    all_durations = []
    all_solutions = []
    all_solutions_values = []

    for _ in range(num_runs):
        start_time = time.perf_counter_ns()
        result = genetic_subset_sum(s, t, 20, 100, 0.6)
        end_time = time.perf_counter_ns()
        
        final_subset = [s[i] for i in range(len(result[0])) if result[0][i] == 1]
        final_sum = sum(final_subset)
        
        sum_solutions += final_sum
        all_durations.append(end_time - start_time)
        all_solutions.append(final_subset) 
        all_solutions_values.append(final_sum)

        if final_sum <= t:
            if final_sum > best_value:
                best_value = final_sum
                best_solution = final_subset

        if final_sum == t:
            find_solution += 1

    
    avg_duration = sum(all_durations) / num_runs
    avg_solutions = sum_solutions / num_runs

    if (find_solution == 0):
        find_solution = all_solutions_values.count(best_value)
    
    data = {
        "len" : len (s),
        "t" : t,
        "set" : s,
        "best_final_sum": best_value,
        "best_final_config": str(best_solution),
        "avg_duration": round(avg_duration, 2),  
        "avg_duration_sec": round(avg_duration / 1_000_000_000, 5),  
        "avg_solutions": round(avg_solutions, 2),
        "all_solutions_values": all_solutions_values,
        "all_durations": all_durations,
        "config_o": list_o if list_o != [] else [],
        "value_config_o":  sum(list_o) if list_o != [] else [],
        "find_solution": find_solution,
        "num_runs": num_runs 
    }

    return data
