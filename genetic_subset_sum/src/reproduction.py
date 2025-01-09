from typing import Callable
import random

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
        mutation_index = random.randint(0, len(parent_x[0])-1)
        child_x[0][mutation_index] = invert(child_x[0][mutation_index])

    for _ in range(qty_mutation_y):
        mutation_index = random.randint(0, len(parent_y[0])-1)
        child_y[0][mutation_index] = invert(child_y[0][mutation_index])

    return child_x, child_y


def generate_children(parents: (list[int],list[int], int),
                      reproduction_method: Callable[[list[int],list[int]],tuple[list[int],list[int]]],
                      new_population: list[list[int]],
                      children_generated: int
                      ):

    child1, child2 = reproduction_method(parents[0], parents[1])
    new_population.append(child1)
    new_population.append(child2)
    children_generated += 2

    return new_population, children_generated

