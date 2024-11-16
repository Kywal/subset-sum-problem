import time
from src.approx_subset_sum import approx_subset_sum
from src.manager_tests import read_file, write_report, print_readme


print_readme()
test_name = input()

s = read_file("datatest/" + test_name + "_w.txt")
list_t = read_file("datatest/" + test_name + "_c.txt")
t = list_t[0] if list_t else -1

if s and list_t:

    start_time = time.perf_counter_ns()
    result = approx_subset_sum(s,t,0.4)
    end_time = time.perf_counter_ns()

    list_o = read_file("datatest/" + test_name + "_o.txt")

    data = {
        "t" : t,
        "set" : s,
        "final_sum": result[0],
        "final_config" :str(result[1]),
        "duration": end_time - start_time,
        "config_o": list_o if list_o != [] else []
    }

    file_name = test_name + ".txt"
    write_report(file_name, data)

else:
    print("Não foi possível processar a instância especificada. Verifique se ela se encontra em datatest no formato indicado.")