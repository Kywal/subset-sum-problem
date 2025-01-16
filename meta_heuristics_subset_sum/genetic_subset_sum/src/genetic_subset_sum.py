from meta_heuristics_subset_sum.genetic_subset_sum.src.population_generator import generate_first_population, generate_new_population
from meta_heuristics_subset_sum.genetic_subset_sum.src.avaliation import sum_p, calculate_fitness_of_all_population, select_next_generation_parents
from meta_heuristics_subset_sum.genetic_subset_sum.src.mergesort import mergesort_populations

from math import floor


def genetic_subset_sum(multiset: list[int], target: int, population_size: int, generations: int, setting_degree_init: float = 0.6, gamma: float = 0.999, mutation_percentage: float = 0.5):
    population = generate_first_population(multiset, target, population_size)
    setting_diff_degree = setting_degree_init
    best_specimen = []

    for generation in range(generations):
        population.sort(key = lambda specimen : specimen[1])
        best_specimen = population[0]

        if best_specimen[1] == 0:
            return best_specimen

        children_generated = 0
        new_population = []

        elite_percentage = 0.5
        elite_upper_bound = floor(len(population) * elite_percentage)
        fittest_population = population[:elite_upper_bound]

        parent_candidates = fittest_population

        while children_generated < population_size:
            try:
                parents = select_next_generation_parents(parent_candidates, children_generated, population_size)
            except ValueError as e:
                print(e)
                return best_specimen
            new_children,  children_generated, new_parents = generate_new_population(
                parents,
                population_size,
                children_generated,
                setting_diff_degree,
                mutation_percentage
            )

            parent_candidates = new_parents
            new_population += new_children

        new_population = calculate_fitness_of_all_population(multiset, target, new_population)
        population = calculate_fitness_of_all_population(multiset, target, population)
        setting_diff_degree = gamma * setting_diff_degree

        population.sort(key = lambda specimen : specimen[1])
        new_population.sort(key = lambda specimen : specimen[1])
        population = mergesort_populations(population, new_population, population_size)
        best_specimen = population[0]
        

    return best_specimen