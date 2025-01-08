from reproduction import crossover, mutate, generate_first_population, generate_new_population
from avaliation import fitness, difference_degree, select_next_generation_parents


def genetic_subset_sum(w: list[int], c: int, population_size: int, generations: int, setting_degree_init: int, gamma:float = 0.9):
    multiset_size = len(w)
    population = generate_first_population(multiset_size, population_size)

    setting_diff_degree = setting_degree_init

    for generation in range(generations):
        
        # falta ver onde chamar fitness

        # antes de entrar no proximo loop que escolhe entre crossover e mutate precijamos ja ver se alcancou a soma objetivo
        # if melhor == c: 
        #   return melhor

        children_generated = 0
        new_population = []

        while children_generated < population_size:

            parents = select_next_generation_parents(population, children_generated)
            newpopulation_qtychildren = generate_new_population(parents, setting_diff_degree)

            new_population = newpopulation_qtychildren[0]
            children_generated = newpopulation_qtychildren[1]

            setting_diff_degree = gamma * setting_diff_degree

        population = new_population[:population_size]

    # se o for acaba (ou seja, limite de geracoes) retornamos o melhor aqui
    # return melhor
