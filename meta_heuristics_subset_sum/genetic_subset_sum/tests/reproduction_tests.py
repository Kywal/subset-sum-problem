from meta_heuristics_subset_sum.genetic_subset_sum.src.reproduction import *
from meta_heuristics_subset_sum.genetic_subset_sum.tests.population_generator_tests import print_specimen


def crossover_test(multiset: list[int], parent_x: [list[int], int], parent_y: [list[int], int]):
    child1, child2 = crossover(parent_x, parent_y)
    print_specimen(multiset, child1)
    print_specimen(multiset, child2)

def mutate_test(multiset: list[int], parent_x: [list[int], int], parent_y: [list[int], int]):
    child1, child2 = mutate(parent_x, parent_y)
    print("child1 ->", end=" ")
    print_specimen(multiset, child1)
    print("child2 ->", end=" ")
    print_specimen(multiset, child2)

multiset = [1, 2, 3, 4, 5, 6, 7, 8]
# crossover_test(multiset, [[1,0,0,0], 0], [[1,1,1,0], 0])

for _ in range(30):
    mutate_test(multiset, [[1,0,0,0,1,0,0,1,0], 0], [[1,1,1,0,0,0,0,0,0], 0])
