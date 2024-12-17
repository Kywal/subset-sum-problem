import os
import time
from exact_subset_sum.src.exact_subset_sum import all_subset_sums
from utils.instance_generator.instance_generator import instance_generator

def read_file(file_name):
    msg = "Erro: O arquivo para o caso de testes " + file_name + " não está no formato adequado."
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
            if len(lines) < 3:
                print(msg)
                return [], [], []
            else:
                try:
                    t = int(lines[0].strip())
                except ValueError:
                    print(msg)
                    return [], [], []

                try:
                    s = [int(x) for x in lines[1].strip()[1:-1].split(",")]
                except ValueError:
                    print(msg)
                    s = []
                
                try:
                    o = [int(x) for x in lines[2].strip()[1:-1].split(",")]
                except ValueError:
                    print(msg)
                    o = []
        return t, s, o

    except FileNotFoundError:
        print(f"O arquivo para o caso de testes '{file_name}' não foi encontrado.")
        return [], [], []
    except ValueError:
        print(msg)
        return [], [], []


def write_report(file_name, data, folder="reports_exact"):

    if  data['config_o'] != [] :
        config_o = str(data['config_o'])
        sum_o = str(sum(data['config_o']))
        dist = str(round(100*((abs(data['final_sum']-sum(data['config_o'])))/sum(data['config_o'])),2))
        
    else:
        config_o = "Não fornecida."
        sum_o = "Não fornecida."
        dist = "--"

    content = (
        f"-------------------\n"
        f"DADOS DA INSTÂNCIA \n"
        f"-------------------\n"
        f"Tamanho do conjunto: {data['len']} \n"
        f"Soma objetivo: {data['t']}\n"
        f"Soma da configuração ótima fornecida: {sum_o}\n" 
        f"-----------\n"
        f"RESULTADOS\n"
        f"-----------\n"
        f"Soma resultante: {data['final_sum']}\n"
        f"Duração da execução (nanosegundos): {data['duration']}\n"
        f"Duração da execução (segundos): {data['duration_sec']}\n\n"
    )

    print(content)
    content += (f"-----------\n"
        f"DETALHAMENTO\n"
        f"-----------\n"
        f"Multiset: {data['set']}\n"
        f"Configuração ótima fornecida: {config_o}\n")

    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, file_name)
    with open(path, 'w') as file:
        file.write(content)

    print(f"Arquivo salvo em: {path}. Acesse para mais detalhes.")
    return path

def menu(item_menu):
    while True:  
        if(item_menu == "1"):
            test_name = input("Informe o nome da instância que deseja executar (ex.: p01, p02...):")
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
                write_report(file_name, data)
                print("------------------------------------------------")
                item_menu = input("Digite 0 para voltar ao menu ou 4 para encerrar.")
            else:
                print("Não foi possível processar a instância especificada. ")
                item_menu = input("Digite 0 para voltar ao menu ou 4 para encerrar.")
        elif (item_menu == '2'):
            print("Para criar uma nova instância aleatória será necessário informar"
            f"\n - Quantidade de elementos do conjunto "
            f"\n - Intervalo no qual os números se encontram (início e fim positivos)")
            set_len = int(input("Quantidade de elementos do conjunto: "))
            set_start = int(input("Início do intervalo de números: "))
            set_end = int(input("Final do intervalo de números: "))

            instance_generator(set_len, (set_start, set_end))

            item_menu = '1'
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
    print("(1) Se deseja executar numa instância que já se encontra na pasta digite 1.")
    print("(2) Para gerar uma nova instância aleatória digite 2.")
    print("(3) Para instruções sobre instâncias específicas.")
    print("(4) Para encerrar digite 4")
    print("(0) Exibir o menu novamente.")