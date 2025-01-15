from meta_heuristics_subset_sum.genetic_subset_sum.src.avaliation import *
from meta_heuristics_subset_sum.genetic_subset_sum.src.mergesort import mergesort_populations
from meta_heuristics_subset_sum.genetic_subset_sum.tests.avaliation_tests import *

target = 4

multiset = [i for i in range(4)]

pop: [list[list[int], int]] = [
    [[0, 1, 1, 0], -1],
    [[1, 0, 0, 0], -1],
    [[1, 1, 1, 0], -1],
    [[0, 0, 0, 0], -1],
]

new_pop: [list[list[int], int]] = [
    [[0, 1, 0, 1], -1],
    [[0, 1, 1, 1], -1],
    [[0, 0, 0, 1], -1],
    [[0, 1, 0, 0], -1],
]

pop_size = 5

print(multiset)
calc_fit_all_pop_test(multiset, target, pop + new_pop)

# print(mergesort_populations(pop, new_pop, pop_size))
