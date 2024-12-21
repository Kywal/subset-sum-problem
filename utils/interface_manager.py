import os
from utils.instance_generator.instance_generator import instance_generator
from utils.file_manager.read_file import read_file
from utils.file_manager.write_report import write_report
from utils.run_algs import run_exact_fft, run_exact_simple, run_aprox, run_exact_mp

def menu(item_menu):

    while True:  
        if(item_menu == "7"):

            test_name = input("(EXATO MP) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file("datatest/" + test_name + ".txt")
            if s and t:
                data = run_exact_mp(t,s,list_o)
                file_name = test_name + ".txt"
                write_report(file_name, data, "exact", "reports_exact_mp")
                print("-" * 30)
                item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")
            else:
                print("Não foi possível processar a instância especificada.")
                item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")

        elif(item_menu == "0"):

            test_name = input("(EXATO FFT) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file("datatest/" + test_name + ".txt")
            if s and t:
                data = run_exact_fft(t,s,list_o)
                file_name = test_name + ".txt"
                write_report(file_name, data, "exact", "reports_exact_fft")
                print("-" * 30)
                item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")
            else:
                print("Não foi possível processar a instância especificada.")
                item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")

        if(item_menu == "1"):

            test_name = input("(EXATO SIMPLE) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file("datatest/" + test_name + ".txt")
            if s and t:
                data = run_exact_simple(t,s,list_o)
                file_name = test_name + ".txt"
                write_report(file_name, data, "exact", "reports_exact_simple")
                print("-" * 30)
                item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")
            else:
                print("Não foi possível processar a instância especificada.")
                item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")

        elif(item_menu == "2"):

            test_name = input("(APROXIMATIVO) Informe o nome da instância que deseja executar (ex.: p01, p02...):\n")
            t,s,list_o = read_file("datatest/" + test_name + ".txt")
            if s and t:
                data = run_aprox(t,s,list_o)
                file_name = test_name + ".txt"
                write_report(file_name, data, "aprox", "reports_aprox")
                print("-" * 30)
                item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")
            else:
                print("Não foi possível processar a instância especificada.")
                item_menu = input("Digite 6 para voltar ao menu ou 5 para encerrar.\n")

        elif (item_menu == '3'):
            print("-" * 30)
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
            print("-" * 50)
            print("Para criar uma nova instância aleatória será necessário informar: \n"
            f" - Quantidade de elementos do conjunto \n"
            f" - Intervalo no qual os números se encontram (início e fim positivos)")
            print("-" * 50)
            set_len = int(input("Quantidade de elementos do conjunto: \n"))
            set_start = int(input("Início do intervalo de números: \n"))
            set_end = int(input("Final do intervalo de números: \n"))
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
    print("(3) Para instruções sobre instâncias específicas.")
    print("(4) Para gerar uma nova instância aleatória digite 4.")
    print("(5) Para encerrar digite 5.")
    print("(6) Exibir o menu novamente.")
