from population_generator import generate_first_population, generate_new_population
from avaliation import sum_p, calculate_fitness_of_all_population, select_next_generation_parents


def genetic_subset_sum(multiset: list[int], target: int, population_size: int, generations: int, setting_degree_init: int, gamma:float = 0.9):
    population = generate_first_population(multiset, target, population_size)
    setting_diff_degree = setting_degree_init
    best_specimen = []

    for generation in range(generations):

        # sort first population by fitness
        population.sort(key = lambda specimen : specimen[1])
        best_specimen = population[0]

        if sum_p(best_specimen[0], multiset) == target:
            return best_specimen

        children_generated = 0
        new_population = []

        while children_generated < population_size:

            parents = select_next_generation_parents(population, children_generated)
            new_population, children_generated = generate_new_population(
                parents,
                population_size,
                children_generated,
                setting_diff_degree
            )

            new_population = calculate_fitness_of_all_population(multiset, target, new_population)
            setting_diff_degree = gamma * setting_diff_degree

        population = new_population[:population_size]
        population.sort(key=lambda specimen: specimen[1])
        best_specimen = population[0]

    return best_specimen