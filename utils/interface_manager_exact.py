import os
import time
from exact_subset_sum.src.exact_subset_sum import all_subset_sums
from cormen_approximation_scheme.src.approx_subset_sum import approx_subset_sum
from utils.instance_generator.instance_generator import instance_generator
from utils.file_manager.read_file import read_file
from utils.file_manager.write_report import write_report

def menu(item_menu):
    while True:  
        if(item_menu == "1"):
            test_name = input("(EXATO) Informe o nome da instância que deseja executar (ex.: p01, p02...):")
            t,s,list_o = read_file("datatest/" + test_name + ".txt")
            if s and t:
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

                file_name = test_name + ".txt"
                write_report(file_name, data, "exact", "reports_exact")
                print("------------------------------------------------")
                item_menu = input("Digite 0 para voltar ao menu ou 5 para encerrar.")
            else:
                print("Não foi possível processar a instância especificada. ")
                item_menu = input("Digite 0 para voltar ao menu ou 5 para encerrar.")
        if(item_menu == "2"):
            test_name = input("(APROXIMATIVO) Informe o nome da instância que deseja executar (ex.: p01, p02...):")
            t,s,list_o = read_file("datatest/" + test_name + ".txt")
            if s and t:
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

                file_name = test_name + ".txt"
                write_report(file_name, data, "aprox", "reports_aprox")
                print("------------------------------------------------")
                item_menu = input("Digite 0 para voltar ao menu ou 5 para encerrar.")
            else:
                print("Não foi possível processar a instância especificada. ")
                item_menu = input("Digite 0 para voltar ao menu ou 5 para encerrar.")
        elif (item_menu == '3'):
            print("-------------------------------------------------------------")
            print(f"(INSTRUÇÕES) Para adicionar uma instância de teste específica, crie na pasta datatest o arquivo <nome_da_instância>.txt com o seguinte formato:\n",
            f"<valor da soma>\n",
            f"<lista de valores do conjunto>\n",
            f"<lista com valores da solução ótima, se houver, se não for possível fornecer, deixe uma lista vazia []>\n")
            print("Exemplo de arquivo:\n",
            f"53\n",
            f"[15, 22, 14, 26, 32, 9,16, 8]\n",
            f"[22,14,9,8]\n")
            print_menu()
            item_menu = input()
        elif (item_menu == '4'):
            print("Para criar uma nova instância aleatória será necessário informar"
            f"\n - Quantidade de elementos do conjunto "
            f"\n - Intervalo no qual os números se encontram (início e fim positivos)")
            set_len = int(input("Quantidade de elementos do conjunto: "))
            set_start = int(input("Início do intervalo de números: "))
            set_end = int(input("Final do intervalo de números: "))

            instance_generator(set_len, (set_start, set_end))

            item_menu = '1'
       
        elif (item_menu == '5'):
            break
        elif (item_menu == '0'):
            print_menu()
            item_menu = input()
        else:
            print("Entrada inválida. Escolha um item do menu:")
            item_menu = input()

def subset_sum_ascii_banner():

    subset_sum = (
        "  █████████  █████  █████ ███████████   █████████  ██████████ ███████████     █████████  █████  █████ ██████   ██████\n"
        " ███░░░░░███░░███  ░░███ ░░███░░░░░███ ███░░░░░███░░███░░░░░█░█░░░███░░░█    ███░░░░░███░░███  ░░███ ░░██████ ██████\n"
        "░███    ░░░  ░███   ░███  ░███    ░███░███    ░░░  ░███  █ ░ ░   ░███  ░    ░███    ░░░  ░███   ░███  ░███░█████░███\n"
        "░░█████████  ░███   ░███  ░██████████ ░░█████████  ░██████       ░███       ░░█████████  ░███   ░███  ░███░░███ ░███\n"
        " ░░░░░░░░███ ░███   ░███  ░███░░░░░███ ░░░░░░░░███ ░███░░█       ░███        ░░░░░░░░███ ░███   ░███  ░███ ░░░  ░███\n"
        " ███    ░███ ░███   ░███  ░███    ░███ ███    ░███ ░███ ░   █    ░███        ███    ░███ ░███   ░███  ░███      ░███\n"
        "░░█████████  ░░████████   ███████████ ░░█████████  ██████████    █████      ░░█████████  ░░████████   █████     █████\n"
        "  ░░░░░░░░░    ░░░░░░░░   ░░░░░░░░░░░   ░░░░░░░░░  ░░░░░░░░░░    ░░░░░        ░░░░░░░░░    ░░░░░░░░   ░░░░░     ░░░░░"
    )

    return subset_sum

def print_menu():
    print("------------------------ MENU ----------------------------")
    print("(1) Digie 1 para executar o EXATO numa instância que já se encontra na pasta.")
    print("(2) Digie 2 para executar o APROXIMATIVO numa instância que já se encontra na pasta.")
    print("(3) Para instruções sobre instâncias específicas.")
    print("(4) Para gerar uma nova instância aleatória digite 4.")
    print("(5) Para encerrar digite 5")
    print("(0) Exibir o menu novamente.")