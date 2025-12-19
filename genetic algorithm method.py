import numpy as np

def init_pop(pop_size):
    return np.random.randint(5, size=(pop_size, 5))

def calc_fitness(population):
    fitness_vals = []
    for x in population:
        penalty = 0
        for i in range(5):
            r = x[i]
            for j in range(5):
                if i == j:
                    continue
                d = abs(i - j)
                if x[j] in [r, r-d, r+d]:
                    penalty += 1
        fitness_vals.append(penalty)
    return -1 * np.array(fitness_vals)

def selection(population, fitness_vals):
    probs = fitness_vals.copy()
    probs += abs(probs.min()) + 1
    probs = probs/probs.sum()
    N = len(population)
    indices = np.arange(N)
    selected_indices = np.random.choice(indices, size=N, p=probs)
    selected_population = population[selected_indices]
    return selected_population

def crossover(parent1, parent2, pc):
    r = np.random.random()
    if r < pc:
        m = np.random.randint(1, 5)
        child1 = np.concatenate([parent1[:m], parent2[m:]])
        child2 = np.concatenate([parent2[:m], parent1[m:]])
    else:
        child1 = parent1.copy()
        child2 = parent2.copy()
    return child1, child2

def mutation(individual, pm):
    r = np.random.random()
    if r < pm:
        m = np.random.randint(5)
        individual[m] = np.random.randint(5)
    return individual

def crossover_mutation(selected_pop, pc, pm):
    N = len(selected_pop)
    new_pop = np.empty((N, 5), dtype=int)
    for i in range(0, N, 2):
        parent1 = selected_pop[i]
        parent2 = selected_pop[i+1]
        child1, child2 = crossover(parent1, parent2, pc)
        new_pop[i] = child1
        new_pop[i+1] = child2
    for i in range(N):
        mutation(new_pop[i], pm)
    return new_pop

def five_queens(pop_size, max_generations, pc=0.7, pm=0.01):
    population = init_pop(pop_size)
    best_fitness_overall = None
    for i_gen in range(max_generations):
        fitness_vals = calc_fitness(population)
        best_i = fitness_vals.argmax()
        best_fitness = fitness_vals[best_i]
        if best_fitness_overall is None or best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            best_solution = population[best_i]
        print(f'\rgen={i_gen+1:06} -f={-best_fitness:03}', end='')
        if best_fitness == 0:
            print('\nFound optimal solution')
            break
        selected_pop = selection(population, fitness_vals)
        population = crossover_mutation(selected_pop, pc, pm)
    print()
    print(best_solution)

five_queens(pop_size=10, max_generations=1000, pc=0.5, pm=0.05)
