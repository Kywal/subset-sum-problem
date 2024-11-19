import os
import time
from src.approx_subset_sum import approx_subset_sum

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            list_s = [int(line.strip()) for line in file]
        return list_s
    except FileNotFoundError:
        print(f"O arquivo para o caso de testes '{file_name}' não foi encontrado.")
        return []
    except ValueError:
        print(f"Erro: O arquivo para o caso de testes '{file_name}' contém dados não numéricos.")
        return []


def write_report(file_name, data, folder="reports"):

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
        f"Multiset: {data['set']}\n"
        f"Soma objetivo: {data['t']}\n"
        f"Configuração ótima fornecida: {config_o}\n" 
        f"Soma da configuração ótima fornecida: {sum_o}\n" 
        f"-----------\n"
        f"RESULTADOS\n"
        f"-----------\n"
        f"Soma resultante (aproximação): {data['final_sum']}\n"
        f"Configuração geradora da aproximação: {data['final_config']}\n"
        f"Duração da execução (nanosegundos): {data['duration']}\n\n"
        f"Solução aproximada se encontra à {dist}% de distância da solução ótima fornecida.\n" 
    )
    print(content)

    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, file_name)
    with open(path, 'w') as file:
        file.write(content)

    print(f"Arquivo salvo em: {path}")
    return path


def print_readme():
    print("----------------------- SUBSET SUM ----------------------")
    print(f"(INSTRUÇÕES) Para adicionar uma nova instância de teste, crie na pasta datatest os arquivos:",
      f"\n<nome_da_instância>_c.txt (contendo o número da soma objetivo)",
      f"\n<nome_da_instância>_w.txt (contendo os valores do conjunto separados por quebra de linha)")
    print("------------------------ MENU ----------------------------")
    print("(1) Se deseja executar numa instância que já se encontra na pasta no formato especificado digite 1.")
    print("(2) Para gerar uma instância digite 2.")
    print("(3) Para encerrar digite 3.")
    print("(0) Exibir o menu novamente.")

def menu(item_menu):
    while True:  
        if item_menu == '3':
            break
        elif item_menu == '0':
            print_readme()
            item_menu = input()
        elif item_menu == '1': 
            test_name = input("Informe o nome da instância que deseja executar (ex.: p01, p02...):")

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
                item_menu = input("Digite 0 para voltar ao menu ou 3 para encerrar.")
            else:
                print("Não foi possível processar a instância especificada. Verifique se ela se encontra em datatest no formato indicado.")
        elif item_menu == '2':
            print("Para criar uma nova instância aleatória será necessário informar"
            f"\n - Quantidade de elementos do conjunto "
            f"\n - Intervalo no qual os números se encontram (início e fim positivos)")
            set_len = int(input("Quantidade de elementos do conjunto:"))
            set_start = int(input("Início do intervalo de números:"))
            set_end = int(input("Final do intervalo de números:"))
            item_menu = '1'
        else:
            print("Entrada inválida. Escolha um item do menu:")
            item_menu = input()

