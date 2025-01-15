import os
from utils.instance_generator.instance_generator import instance_generator
from utils.file_manager.read_file import read_file
from utils.file_manager.write_report import write_report,  write_report_mult
from utils.run_algs import run_exact_fft, run_exact_simple, run_aprox, run_exact_mp,  run_genetic, run_genetic_many_times

def menu(item_menu):

    datatest_path = "all_datatests/datatest/"
    report_path = "all_reports/"
    file_type = ".txt"

    report_aprox_path = report_path + "reports_aprox"
    report_exact_fft_path = report_path + "reports_exact_ff"
    report_exact_mp_path = report_path + "reports_exact_mp"
    report_exact_simple_path = report_path + "reports_exact_simple"
    report_genetic_path = report_path + "reports_genetic"

    while True:  
        if(item_menu == "7"):

            test_name = input("(EXATO MP) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file(datatest_path + test_name + file_type)
            if s and t:
                data = run_exact_mp(t,s,list_o)
                file_name = test_name + file_type
                write_report(file_name, data, "exact", report_exact_mp_path)
                item_menu = ending_report_writing_process()
            else:
                item_menu = instance_processing_error()

        elif (item_menu == '8'):
            test_name = input("(GENETICO) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file(datatest_path + test_name + file_type)
            if s and t:
                data = run_genetic(t,s,list_o)
                file_name = test_name + file_type
                write_report(file_name, data, "genetic", report_genetic_path)
                item_menu = ending_report_writing_process()
            else:
                item_menu = instance_processing_error()
        elif (item_menu == '9'):
            test_name = input("(GENETICO TESTES) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file(datatest_path + test_name + file_type)
            if s and t:
                data = run_genetic_many_times(t,s,list_o)
                file_name = "mult_" + test_name + file_type
                write_report_mult(file_name, data, "genetic", report_genetic_path)
                item_menu = ending_report_writing_process()
            else:
                item_menu = instance_processing_error()
        elif (item_menu == '10'):
            run_all_tests(datatest_path, file_type, report_genetic_path)
           
        elif(item_menu == "0"):

            test_name = input("(EXATO FFT) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file(datatest_path + test_name + file_type)
            if s and t:
                data = run_exact_fft(t,s,list_o)
                file_name = test_name + file_type
                write_report(file_name, data, "exact", report_exact_fft_path)
                item_menu = ending_report_writing_process()
            else:
                item_menu = instance_processing_error()

        if(item_menu == "1"):

            test_name = input("(EXATO SIMPLE) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file(datatest_path + test_name + file_type)
            if s and t:
                data = run_exact_simple(t,s,list_o)
                file_name = test_name + file_type
                write_report(file_name, data, "exact", report_exact_simple_path)
                item_menu = ending_report_writing_process()
            else:
                item_menu = instance_processing_error()

        elif(item_menu == "2"):

            test_name = input("(APROXIMATIVO) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file(datatest_path + test_name + file_type)
            if s and t:
                data = run_aprox(t,s,list_o)
                file_name = test_name + file_type
                write_report(file_name, data, "aprox", report_aprox_path)
                item_menu = ending_report_writing_process()
            else:
                item_menu = instance_processing_error()

        elif (item_menu == '3'):
            print_add_instance_instructions()
            print_menu()
            item_menu = input()

        elif (item_menu == '4'):
            set_len, set_start, set_end = generate_instance_process()
            instance_generator(set_len, (set_start, set_end))
            print_menu()
            item_menu = input()

        elif (item_menu == '5'):
            break

        elif (item_menu == '6'):
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
    print("+" + "-" * 30 + "+")
    print("|" + " " * 11 + "MENU" + " " * 15 + "|")
    print("+" + "-" * 30 + "+")
    print("(0) Digite 0 para executar o EXATO FFT numa instância que já se encontra na pasta.")
    print("(1) Digite 1 para executar o EXATO SIMPLES numa instância que já se encontra na pasta.")
    print("(2) Digite 2 para executar o APROXIMATIVO numa instância que já se encontra na pasta.")
    print("(7) Digite 7 para executar o EXATO MP numa instância que já se encontra na pasta.")
    print("(8) Digite 8 para executar o GENETICO numa instância que já se encontra na pasta.")
    print("(3) Para instruções sobre instâncias específicas.")
    print("(4) Para gerar uma nova instância aleatória digite 4.")
    print("(5) Para encerrar digite 5.")
    print("(6) Exibir o menu novamente.")

def print_add_instance_instructions():
    print("-" * 30)
    print(
        f"(INSTRUÇÕES) Para adicionar uma instância de teste específica, crie na pasta datatest o arquivo <nome_da_instância>.txt com o seguinte formato:\n",
        f"<valor da soma>\n",
        f"<lista de valores do conjunto>\n",
        f"<lista com valores da solução ótima, se houver, se não for possível fornecer, deixe uma lista vazia []>\n")
    print("Exemplo de arquivo:\n",
          f"53\n",
          f"[15, 22, 14, 26, 32, 9,16, 8]\n",
          f"[22,14,9,8]\n")

def generate_instance_process():
    print("-" * 50)
    print("Para criar uma nova instância aleatória será necessário informar: \n"
          f" - Quantidade de elementos do conjunto \n"
          f" - Intervalo no qual os números se encontram (início e fim positivos)")
    print("-" * 50)
    set_len = int(input("Quantidade de elementos do conjunto: \n"))
    set_start = int(input("Início do intervalo de números: \n"))
    set_end = int(input("Final do intervalo de números: \n"))

    return set_len, set_start, set_end

def instance_processing_error():
    print("Não foi possível processar a instância especificada.")
    item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")
    
    return item_menu

def ending_report_writing_process():
    qty_dashes_after_write_report = 30

    print("-" * qty_dashes_after_write_report)
    item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")
    return item_menu

def run_all_tests(datatest_path, file_type, report_genetic_path):
    grouped_durations = []
    grouped_distances = []
    grouped_distances_avg = []
    all_durations = []
    all_distances = []
    all_distances_avg = []

    for i in range(1, 26):
        test_name = f"p{i:02d}"
        t, s, list_o = read_file(datatest_path + test_name + file_type)
        if s and t:
            data = run_genetic_many_times(t, s, list_o)
            
            all_durations.append(data['avg_duration'])
            all_distances.append(round(100*((abs(data['best_final_sum']-sum(data['config_o'])))/sum(data['config_o'])),2))
            all_distances_avg.append(round(100*((abs(data['avg_solutions']-sum(data['config_o'])))/sum(data['config_o'])),2))
            
            if i % 5 == 0:
                print(all_durations[-5:])
                avg_duration_group = calculate_average(all_durations[-5:])
                avg_distance_group = calculate_average(all_distances[-5:])
                avg_distance_avg_group = calculate_average(all_distances_avg[-5:])
                grouped_durations.append(avg_duration_group)
                grouped_distances.append(avg_distance_group)
                grouped_distances_avg.append(avg_distance_avg_group)
                
            file_name = f"mult_{test_name}{file_type}"
            write_report_mult(file_name, data, "genetic", report_genetic_path)

    avg_duration_total = round(sum(all_durations) / len(all_durations), 2)
    avg_distance_total = round(sum(all_distances) / len(all_distances), 2)
    avg_distance_avg_total = round(sum(all_distances_avg) / len(all_distances_avg), 2)

    print("Médias das durações por grupo:", grouped_durations)
    print("Médias das distâncias da melhor para a ótima por grupo:", grouped_distances)
    print("Médias das distâncias da média das soluções para a ótima por grupo:", grouped_distances_avg)
    print("Média geral de durações:", avg_duration_total)
    print("Média geral de distâncias entre a melhor e a ótima:", avg_distance_total)
    print("Média geral de distâncias entre a melhor e a média:", avg_distance_avg_total)



def calculate_average(data_list):
    return round(sum(data_list) / len(data_list), 2)