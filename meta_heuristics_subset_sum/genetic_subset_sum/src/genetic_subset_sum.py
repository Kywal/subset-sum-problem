from meta_heuristics_subset_sum.genetic_subset_sum.src.population_generator import generate_first_population, generate_new_population
from meta_heuristics_subset_sum.genetic_subset_sum.src.avaliation import sum_p, calculate_fitness_of_all_population, select_next_generation_parents
from meta_heuristics_subset_sum.genetic_subset_sum.src.mergesort import mergesort_populations

from math import floor


def genetic_subset_sum(multiset: list[int], target: int, population_size: int, generations: int, setting_degree_init: float = 0.6, gamma: float = 0.999, mutation_percentage: float = 0.5):
    population = generate_first_population(multiset, target, population_size)
    setting_diff_degree = setting_degree_init

    # sort first population by fitness
    population.sort(key = lambda specimen : specimen[1])
    best_specimen = population[0]

    for generation in range(generations):
        print(best_specimen)

        if sum_p(best_specimen[0], multiset) == target:
            return best_specimen

        children_generated = 0
        new_population = []

        elite_percentage = 0.5
        elite_upper_bound = floor(len(population) * elite_percentage)
        fittest_population = population[:elite_upper_bound]

        while children_generated < population_size:
            try:
                parents = select_next_generation_parents(fittest_population, children_generated, len(population))
            except ValueError as e:
                print(e)
                print(best_specimen)
                return best_specimen
            new_children, children_generated = generate_new_population(
                parents,
                population_size,
                children_generated,
                setting_diff_degree,
                mutation_percentage
            )

            new_population += new_children

        setting_diff_degree = gamma * setting_diff_degree

        new_population = calculate_fitness_of_all_population(multiset, target, new_population)
        population = calculate_fitness_of_all_population(multiset, target, population)

        population.sort(key=lambda specimen: specimen[1])
        new_population.sort(key=lambda specimen: specimen[1])

        population = mergesort_populations(population, new_population, population_size)

        # population = sorted(population + new_population, key=lambda x: x[1])[:population_size]
        # population = new_population
        best_specimen = population[0]

    return best_specimen