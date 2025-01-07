import math
import random

def sum_p(x: list[int], w: list[int]):
    multiset_size = len(x)
    result = 0
    for i in range(multiset_size):
        result += x[i] * w[i]
    return result

def fitness(x: list[int], w: list[int], c: int):
    s = 0
    px = sum_p(x, w)
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

def crossover(parent_x: list[int], parent_y: list[int]):
    point = random.randint(1, len(parent_x) - 1)
    child1 = parent_x[:point] + parent_y[point:]
    child2 = parent_y[:point] + parent_x[point:]
    return child1, child2


# def mutate():
#
# def selection():

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

# def genetic_subset_sum():
