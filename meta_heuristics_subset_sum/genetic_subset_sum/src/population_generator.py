from meta_heuristics_subset_sum.genetic_subset_sum.src.reproduction import crossover, mutate, generate_children
from meta_heuristics_subset_sum.genetic_subset_sum.src.avaliation import fitness
import random


def generate_first_population(multiset: list[int], target: int, population_size: int):
    multiset_size = len(multiset)
    population = []

    for _ in range(0, population_size):
        qty_of_ones_on_dna = random.randint(0, multiset_size)
        specimen = [[0 for _ in range(multiset_size)], -1]

        for _ in range(0, qty_of_ones_on_dna):
            one_index = random.randint(0, multiset_size - 1)
            specimen[0][one_index] = 1

        specimen[1] = fitness(specimen[0], multiset, target)
        population.append(specimen)

    return population

def generate_new_population(parents: list[list[int], list[int], int],
                            population_size: int,
                            children_generated: int,
                            setting_diff_degree: int,
                            mutation_percentage: float
                            ):

    new_population = []
    new_parents = []
    for parent_pair in parents:

        diff_deg = parent_pair[2]

        if diff_deg > setting_diff_degree:
            child1, child2 = crossover(parent_pair[0], parent_pair[1], mutate_percentage)
            new_population.append(child1)
            new_population.append(child2)
            children_generated += 2

    if children_generated == population_size:
        return new_population, children_generated, new_parents

    else:
        for parent_pair in parents:

            diff_deg = parent_pair[2]

            if diff_deg < setting_diff_degree:
                child1, child2 = mutate(parent_pair[0], parent_pair[1], mutate_percentage)
                new_parents.append(child1)
                new_parents.append(child2)

    return new_population, children_generated, new_parents