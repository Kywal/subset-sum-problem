from meta_heuristics_subset_sum.genetic_subset_sum.src.avaliation import *

def test_sum_p(x: list[int], w: list[int]):
    print("specimen = " + str(x))
    print("multiset = " + str(w))
    print("somatorio specimen = " + str(sum_p(x,w)))

# -----------------------------------------

def calc_fit_all_pop_test(multiset: list[int], target: int, population: [list[list[int], int]]):
    print(calculate_fitness_of_all_population(multiset, target, population))

# test_sum_p([0, 0, 0], [4, 4, 4])



