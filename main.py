import time
from src.approx_subset_sum import approx_subset_sum
from src.interface_manager import read_file, write_report, print_readme, menu

print_readme()
item_menu = input()
while True:  
    if item_menu == '3':
        break
    elif item_menu == '0':
        print_readme()
        item_menu = input()
    elif item_menu == '1': 
        menu(item_menu)
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
            print("------------------------------------------------")
            print("Digite 0 para voltar ao menu ou 3 para encerrar.")
            item_menu = input()
        else:
            print("Não foi possível processar a instância especificada. Verifique se ela se encontra em datatest no formato indicado.")
    else:
        print("Entrada inválida. Escolha um item do menu:")
        item_menu = input()