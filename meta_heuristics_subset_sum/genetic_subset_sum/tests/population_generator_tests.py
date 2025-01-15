from meta_heuristics_subset_sum.genetic_subset_sum.src.population_generator import generate_first_population
from meta_heuristics_subset_sum.genetic_subset_sum.src.avaliation import sum_p

def print_specimen(multiset: list[int], spec: [list[int], int]):
    print("solution: " + str(spec[0]) + " --- sum: " + str(sum_p(multiset,spec[0])) +  " ===> fitness: " + str(spec[1]))

def print_population(population: list[int], multiset: list[int]):
    for ind in population:
        print_specimen(multiset, ind)

def generate_first_population_test(multiset: list[int], target: int, population_size: int):
    population = generate_first_population(multiset, target, population_size)
    population.sort(key=lambda s: s[1])
    print_population(population, multiset)

generate_first_population_test([1, 2, 3, 4, 5, 6, 7, 8, 9, 100], 10, 10)
