from typing import Callable
import random
from math import floor

def crossover(parent_x: [list[int], int], parent_y: [list[int], int], mutate_percentage: float):
    child1_list = []
    child2_list = []
    
    for i in range(len(parent_x[0])):
        if random.uniform(0.0, 1.0) < 0.5:
            child1_list.append(parent_x[0][i])
            child2_list.append(parent_y[0][i])
        else:
            child1_list.append(parent_y[0][i])
            child2_list.append(parent_x[0][i])
    
    child1 = (child1_list, -1)
    child2 = (child2_list, -1)
    
    return child1, child2


def mutate(parent_x: [list[int], int], parent_y: [list[int], int], mutate_percentage: float):
    mutation_x_index = floor(mutate_percentage * len(parent_x[0]))
    mutation_y_index = floor(mutate_percentage * len(parent_y[0]))

    qty_mutation_x = random.randint(1, mutation_x_index)
    qty_mutation_y = random.randint(1, mutation_y_index)

    child_x = [parent_x[0], -1]
    child_y = [parent_y[0], -1]

    invert = lambda bin_num :  1 if bin_num == 0 else 1

    for _ in range(qty_mutation_x):
        mutation_index = random.randint(0, len(parent_x[0])-1)
        child_x[0][mutation_index] = invert(child_x[0][mutation_index])

    for _ in range(qty_mutation_y):
        mutation_index = random.randint(0, len(parent_y[0])-1)
        child_y[0][mutation_index] = invert(child_y[0][mutation_index])

    return child_x, child_y


def generate_children(parents: (list[int],list[int], int),
                      reproduction_method: Callable[[list[int],list[int], float], tuple[list[list[int], int],list[list[int], int]]],
                      new_population: list[list[int], int],
                      children_generated: int,
                      mutate_percentage: float,
                      ):

    child1, child2 = reproduction_method(parents[0], parents[1], mutate_percentage)
    new_population.append(child1)
    new_population.append(child2)
    children_generated += 2

    return new_population, children_generated

