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
        f"Soma resultante (aproximação): {data['final_sum']}\n"
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