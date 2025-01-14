from meta_heuristics_subset_sum.genetic_subset_sum.src.mergesort import mergesort_populations

pop = [
    [[0, 0, 0, 0], 1],
    [[0, 0, 0, 0], 2],
]

new_pop = [
    [[0, 0, 0, 0], 4],
    [[0, 0, 0, 0], 10],
]

pop_size = 5

print(mergesort_populations(pop, new_pop, pop_size))

