from reproduction import crossover, mutate, generate_children
from avaliation import fitness
import random


def generate_first_population(multiset: list[int], target: int, population_size: int):
    multiset_size = len(multiset)
    population = []

    for _ in range(0, population_size):
        qty_of_ones_on_dna = random.randint(0, multiset_size)
        specimen = [[0 for _ in range(multiset_size)], -1]

        for _ in range(0, qty_of_ones_on_dna):
            one_index = random.randint(0, multiset_size)
            specimen[0][one_index] = 1

        specimen[1] = fitness(specimen[0], multiset, target)
        population.append(specimen)

    return population

def generate_new_population(parents: list[list[int], list[int], int],
                            population_size: int,
                            children_generated: int,
                            setting_diff_degree: int
                            ):

    new_population = []
    for parent_pair in parents:

        diff_deg = parent_pair[2]

        if diff_deg > setting_diff_degree:
            new_population, children_generated = generate_children(
                parent_pair,
                crossover,
                new_population,
                children_generated
            )

    for parent_pair in parents:

        diff_deg = parent_pair[2]

        if diff_deg != setting_diff_degree and children_generated != population_size:
            new_population, children_generated = generate_children(
                parent_pair,
                mutate,
                new_population,
                children_generated
            )

    return new_population, children_generated