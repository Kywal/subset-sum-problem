from typing import Callable
from avaliation import fitness
import random

def generate_first_population(multiset: list[int], target: int, population_size: int):
    multiset_size = len(multiset)
    population = set()

    for _ in range(0, population_size):
        qty_of_ones_on_dna = random.randint(0, multiset_size)
        specimen = [[0 for _ in range(multiset_size)], -1]

        for _ in range(0, qty_of_ones_on_dna):
            one_index = random.randint(0, multiset_size)
            specimen[0][one_index] = 1

        specimen[1] = fitness(specimen[0], multiset, target)
        population.add(specimen)

    return population

def crossover(parent_x: [list[int], int], parent_y: [list[int], int]):
    point = random.randint(1, len(parent_x[0]) - 1)
    child1 = (parent_x[0][:point] + parent_y[0][point:], -1)
    child2 = (parent_y[0][:point] + parent_x[0][point:], -1)
    return child1, child2


def mutate(parent_x: [list[int], int], parent_y: [list[int], int]):
    qty_mutation_x = random.randint(1, len(parent_x[0]))
    qty_mutation_y = random.randint(1, len(parent_y[0]))

    child_x = (parent_x[0], -1)
    child_y = (parent_y[0], -1)

    invert = lambda bin_num :  1 if bin_num == 0 else 1

    for _ in range(qty_mutation_x):
        mutation_index = random.randint(0, len(parent_x[0]))
        child_x[0][mutation_index] = invert(child_x[0][mutation_index])

    for _ in range(qty_mutation_y):
        mutation_index = random.randint(0, len(parent_y[0]))
        child_y[0][mutation_index] = invert(child_y[0][mutation_index])

    return child_x, child_y


def generate_children(parents: (list[int],list[int], int),
                      reproduction_method: Callable[[list[int],list[int]],(list[int],list[int])],
                      new_population: list[list[int]],
                      children_generated: int
                      ):

    child1, child2 = reproduction_method(parents[0], parents[1])
    new_population.append(child1)
    new_population.append(child2)
    children_generated += 2

    return new_population, children_generated


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

