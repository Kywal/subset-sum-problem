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

def genetic_subset_sum(w: list[int], c: int, population_size: int, generations: int, Ds_init: int, gamma:float = 0.9):
    multiset_size = len(w)
    population = generate_first_population(multiset_size, population_size)

    Ds = Ds_init

    for generation in range(generations):
        
        # falta ver onde chamar fitness

        # antes de entrar no proximo loop que escolhe entre crossover e mutate precijamos ja ver se alcancou a soma objetivo
        # if melhor == c: 
        #   return melhor

        nc = 0 
        new_population = []

        while nc < population_size:

            # seleciona par de pais com selection e poe nessas variaveis 
            parent_x = []
            parent_y = []

            di = difference_degree(parent_x, parent_y)

            if di > Ds:
                child1, child2 = crossover(parent_x, parent_y)
                new_population.appent(child1)
                new_population.appent(child2)
                nc += 2
            else:
                child_x, child_y = mutate(parent_x,parent_y)
                new_population.appent(child_x)
                new_population.appent(child_y)
                nc += 2

            Ds = gamma * Ds

        population = new_population[:population_size]

    # se o for acaba (ou seja, limite de geracoes) retornamos o melhor aqui
