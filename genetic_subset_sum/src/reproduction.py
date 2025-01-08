import random

def crossover(parent_x: list[int], parent_y: list[int]):
    point = random.randint(1, len(parent_x) - 1)
    child1 = parent_x[:point] + parent_y[point:]
    child2 = parent_y[:point] + parent_x[point:]
    return child1, child2


def mutate(parent_x: list[int], parent_y: list[int]):
    qty_mutation_x = random.randint(1, len(parent_x))
    qty_mutation_y = random.randint(1, len(parent_y))

    child_x = parent_x
    child_y = parent_y

    invert = lambda bin_num :  1 if bin_num == 0 else 1

    for _ in range(qty_mutation_x):
        mutation_index = random.randint(0, len(parent_x))
        child_x[mutation_index] = invert(child_x[mutation_index])

    for _ in range(qty_mutation_y):
        mutation_index = random.randint(0, len(parent_y))
        child_y[mutation_index] = invert(child_y[mutation_index])

    return child_x, child_y

def generate_first_population(multiset_size: int, population_size: int):
    population = set()

    for _ in range(0, population_size):
        qty_of_ones_on_dna = random.randint(0, multiset_size)

        for _ in range(0, qty_of_ones_on_dna):
            one_index = random.randint(0, multiset_size)

            specimen = [0 for _ in range(multiset_size)]
            specimen[one_index] = 1
            population.add(specimen)

    return population