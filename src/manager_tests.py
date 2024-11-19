import os

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            list_s = [int(line.strip()) for line in file]
        return list_s
    except FileNotFoundError:
        print(f"Erro: O arquivo para o caso de testes expecificado '{file_name}' não foi encontrado. Verifique se existe arquivo correspondente a essa instância na pasta datatest.")
        return []
    except ValueError:
        print(f"Erro: O arquivo para o caso de testes expecificado '{file_name}' contém dados não numéricos.")
        return []


def write_report(file_name, data, folder="reports"):
    content = (
        f"REPORT\n\n"
        f"-------------------\n"
        f"DADOS DA INSTÂNCIA \n"
        f"-------------------\n\n"
        f"Multiset: {data['set']}\n"
        f"Soma objetivo: {data['t']}\n\n"
        f"-----------\n"
        f"RESULTADOS\n"
        f"-----------\n\n"
        f"Soma resultante (aproximação): {data['final_sum']}\n"
        f"Configuração geradora da aproximação: {data['final_config']}\n"
        f"Duração da execução (nanosegundos): {data['duration']}\n"
    )
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, file_name)
    with open(path, 'w') as file:
        file.write(content)

    print(f"Arquivo salvo em: {path}")
    return path