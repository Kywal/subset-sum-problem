import random

def sum_p(x: list[int], w: list[int]):
    multiset_size = len(x)
    result = 0
    for i in range(multiset_size):
        result += x[i] * w[i]
    return result

def fitness(solution: list[int], w: list[int], c: int):
    s = 0
    px = sum_p(solution, w)
    if c - px >= 0:
        s = 1
    return s * (c - px) + (1 - s) * px

def difference_degree(parent_x: list[int], parent_y: list[int]):
    multiset_size = len(parent_x)
    nd = 0
    for i in range(multiset_size):
        if parent_x[i] != parent_y[i]:
            nd += 1
    ng = multiset_size
    return nd / ng

def select_next_generation_parents(population: set[tuple[list[int], int]], children_generated: int):
    population_list = list(population)
    population_size = len(population)
    parent_pairs_qty = (population_size - children_generated) // 2
    parents = []

    for _ in range(parent_pairs_qty):
        first_parent_index = random.randint(0,population_size-1)
        second_parent_index = random.randint(0,population_size-1)

        first_parent = population_list[first_parent_index]
        second_parent = population_list[second_parent_index]
        diff_degree = difference_degree(first_parent[0], second_parent[0])

        parents.append(
            (first_parent, second_parent, diff_degree)
        )

    return parents

def calculate_fitness_of_all_population(multiset: list[int], target: int, population: list[[list[int], int]]):

    for i in range(len(population)):
        individual = population[i]
        fitness_value = fitness(individual[0], multiset, target)
        population[i] = (individual[0], fitness_value)

    return population

