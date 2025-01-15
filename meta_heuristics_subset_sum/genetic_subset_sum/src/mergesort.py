import sys


def mergesort_populations(old_population: [list[list[int], int]], new_population: [list[list[int], int]], population_size: int):
    pop_iter = iter(old_population)
    new_pop_iter = iter(new_population)

    population = []
    default_ind = [[], sys.maxsize]

    counter = 0
    runner_pop = next(pop_iter, default_ind)
    runner_newpop = next(new_pop_iter, default_ind)

    while counter < population_size:

        if runner_pop[1] <= runner_newpop[1]:
            if runner_pop != default_ind:
                population.append(runner_pop)
                runner_pop = next(pop_iter, default_ind)
        else:
            if runner_newpop != default_ind:
                population.append(runner_newpop)
                runner_newpop = next(new_pop_iter, default_ind)

        counter += 1

    return population





