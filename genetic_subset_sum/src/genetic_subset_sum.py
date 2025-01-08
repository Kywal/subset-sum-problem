from reproduction import crossover, mutate, generate_first_population
from avaliation import fitness, difference_degree


def genetic_subset_sum(w: list[int], c: int, population_size: int, generations: int, Ds_init: int, gamma:float = 0.9):
    multiset_size = len(w)
    population = generate_first_population(multiset_size, population_size)

    Ds = Ds_init

    for generation in range(generations):
        
        # falta ver onde chamar fitness

        # antes de entrar no proximo loop que escolhe entre crossover e mutate precijamos ja ver se alcancou a soma objetivo
        # if melhor == c: 
        #   return melhor

        nc = 0 
        new_population = []

        while nc < population_size:

            # seleciona par de pais com selection e poe nessas variaveis 
            parent_x = []
            parent_y = []

            di = difference_degree(parent_x, parent_y)

            if di > Ds:
                child1, child2 = crossover(parent_x, parent_y)
                new_population.appent(child1)
                new_population.appent(child2)
                nc += 2
            else:
                child_x, child_y = mutate(parent_x,parent_y)
                new_population.appent(child_x)
                new_population.appent(child_y)
                nc += 2

            Ds = gamma * Ds

        population = new_population[:population_size]

    # se o for acaba (ou seja, limite de geracoes) retornamos o melhor aqui
    # return melhor
