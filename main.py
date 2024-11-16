import time
from src.approx_subset_sum import approx_subset_sum
from src.manager_tests import read_file, write_report

s = []

print("Informe a instância de teste do datatest que deseja executar (ex.: p01, p02...):")
test_name = input()

s = read_file("datatest/" + test_name + "_w.txt")
list_t = read_file("datatest/" + test_name + "_c.txt")
t = list_t[0] if list_t else -1

start_time = time.perf_counter_ns()
result = approx_subset_sum(s,t,0.4)
end_time = time.perf_counter_ns()

data = {
    "t" : t,
    "set" : s,
    "final_sum": str(result[0]),
    "final_config" :str(result[1]),
    "duration": end_time - start_time
}

file_name = test_name + ".txt"
write_report(file_name, data)
