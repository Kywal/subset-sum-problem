import os

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
