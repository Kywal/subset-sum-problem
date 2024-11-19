import os

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
        f"Duração da execução (nanosegundos): {data['duration']}\n"
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
    print("--------------- SUBSET SUM APROXIMAÇÃO -----------------")
    print(f"(1) Para adicionar uma nova instância de teste, crie na pasta datatest os arquivos:",
      f"\n<nome_da_instância>_c.txt (contendo o número da soma objetivo)",
      f"\n<nome_da_instância>_w.txt (contendo os valores do conjunto separados por quebra de linha)")
    print("---------------------------------------------------------")
    print("(2) Se a instância já se encontra na pasta no formato especificado, selecione-a informando o nome da instância de teste do datatest que deseja executar (ex.: p01, p02...):")