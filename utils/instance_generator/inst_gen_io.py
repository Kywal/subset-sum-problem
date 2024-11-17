import os
import platform


def write_instance(instance: str, folder="datatest"):

    slash = ""
    os_name = platform.system()
    filetype = ".txt"

    match os_name:
        case "Windows":
            slash = "\\"
        case _ :
            slash = "/"

    file_name = "p"
    filenumber = len(os.listdir(folder + slash))

    if filenumber != 0 and filenumber <= 9:
        file_name = folder + slash + file_name + "0" + str(filenumber) + filetype
    elif filenumber > 9:
        file_name = folder + slash + file_name + str(filenumber) + filetype

    file = open(file_name, "w")
    file.write(instance)
    file.close()

    print(f"Arquivo salvo como: {file_name}")


def instance_to_str(ms: list[int], opt_sum: int, opt_config: list[int]):

    instance = (
        f"{opt_sum}\n"
        f"{ms}\n"
        f"{opt_config}\n"
    )

    return instance


