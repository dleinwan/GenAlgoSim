
class Organism:
    def __init__(self) -> None:
        self.fitness = 0
        #randomize genes?
        self.genes = []
        pass

class Population:

    def __init__(self) -> None:
        self.popSize = 10
        self.organisms = []
        for i in range(0,self.popSize):
            self.organisms.append(Organism())
        pass

# START
# Generate the initial population
# Compute fitness
# REPEAT
#     Selection
#     Crossover
#     Mutation
#     Compute fitness
# UNTIL population has converged
# STOP


