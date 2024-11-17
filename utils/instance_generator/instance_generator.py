import random
from utils.instance_generator.inst_gen_io import write_instance, instance_to_str

def instance_generator(s: int , rng: tuple[int, int]):
    validade_inputs(s, rng)
    multiset = generate_multiset(s, rng)
    optimal_sum = generate_optimal_sum(multiset.copy())

    instance = instance_to_str(multiset, optimal_sum[0], optimal_sum[1])
    write_instance(instance)

    return multiset, optimal_sum

def generate_multiset(s: int, rng: tuple[int, int]):
    ms = []

    for i in range(0, s):
        ms.append(random.randint(rng[0], rng[1]))

    return ms

def generate_optimal_sum(ms: list[int]):
    optimal_config = []
    optimal_sum = 0

    size_sum = random.randint(1, len(ms))
    for _ in range(0, size_sum):

        i = random.randint(0, len(ms) - 1)
        optimal_sum += ms[i]
        optimal_config.append(ms[i])
        ms.pop(i)


    return optimal_sum, optimal_config

def validade_inputs(s: int, rng: tuple[int, int]):

    if s < 0:
        raise ValueError("O tamanho do multiset não pode ser negativo!")

    if rng[0] > rng[1]:
        raise ValueError("O intervalo precisa ser definido de forma crescente! Ex: [1,4]")
