import os

def write_report(file_name, data, alg, folder="reports_exact"):

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

    if(alg == "aprox"):
        content += (f"Solução aproximada se encontra à {dist}% de distância da solução ótima fornecida.\n")
   
    print(content)
    content += (f"-----------\n"
        f"DETALHAMENTO\n"
        f"-----------\n"
        f"Multiset: {data['set']}\n"
        f"Configuração ótima fornecida: {config_o}\n"
        f"Configuração geradora da soma resultante: {data['final_config']}\n")
        

    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, file_name)
    with open(path, 'w') as file:
        file.write(content)

    print(f"Arquivo salvo em: {path}. Acesse para mais detalhes.")
    return path


def write_report_mult(file_name, data, alg, folder="reports_exact"):

    if  data['config_o'] != [] :
        config_o = str(data['config_o'])
        sum_o = str(data['value_config_o'])
        dist_best_to_solution = str(round(100*((abs(data['best_final_sum']-sum(data['config_o'])))/sum(data['config_o'])),2))
        dist_avg_to_solution = str(round(100*((abs(data['avg_solutions']-sum(data['config_o'])))/sum(data['config_o'])),2))

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
        f"Melhor soma encontrada: {data['best_final_sum']}\n"
        f"Média das somas encontradas: {data['avg_solutions']}\n"
        f"Media da duração da execução (nanosegundos): {data['avg_duration']}\n"
        f"Media da duração da execução (segundos): {data['avg_duration_sec']}\n\n"
        f"-----------\n"
        f"Melhor solução encontrada se encontra à {dist_best_to_solution}% de distância da solução ótima fornecida.\n"
        f"Média das soluções encontradas se encontra à {dist_avg_to_solution}% de distância da solução ótima fornecida.\n"
        f"-----------\n"
        f"A solução ótima foi alcançada {data['find_solution']} vezes de {data['num_runs']}\n"
        f"Soluções encontradas: {data['all_solutions_values']} \n"

    )

    print(content)

    content += (f"-----------\n"
        f"DETALHAMENTO\n"
        f"-----------\n"
        f"Multiset: {data['set']}\n"
        f"Configuração ótima fornecida: {config_o}\n"
        f"Configuração geradora da soma resultante: {data['best_final_config']}\n")
        

    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, file_name)
    with open(path, 'w') as file:
        file.write(content)

    print(f"Arquivo salvo em: {path}. Acesse para mais detalhes.")
    return path