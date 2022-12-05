# START
# Generate the initial population
# Compute fitness
# REPEAT
#     Selection
#     Crossover
#     Mutation
#     Compute fitness
# UNTIL population has converged (we may instead just run it for a fixed number of generations)
#                                (this way we will not have to deal with computing convergence)
# STOP

class Organism:
    def __init__(self) -> None:
        #TODO: randomize fitness
        self.fitness = 0
        #TODO: randomize genes
        self.genes = []
        pass

# Population is made up of organisms
class Population:
    def __init__(self) -> None:
        #TODO: decide on population size
        self.popSize = 10
        self.organisms = []
        for organism in self.organisms:
            self.organisms.append(Organism())
        pass

def main():
    #TODO: decide on number of generations to run for
    #number of generations algorithm will run for
    numGens = 5

    print("Beginning of Generations")
    currGeneration = Population()

    #TODO: compute fitness
    computeFitness(1, currGeneration)

    for genNum in range(numGens-1):
        # STORE NEW DATA HERE
        nextGeneration = Population()
        print(genNum)

        #TODO: selection (kill off one half)
        selection(genNum, currGeneration, nextGeneration)

        #TODO: crossover (reproduce)
        crossover(genNum, currGeneration, nextGeneration)

        #TODO: mutate
        mutation(genNum, currGeneration, nextGeneration)

        computeFitness(genNum, currGeneration, nextGeneration)

        currGeneration = nextGeneration

        # wait until last generation's music is done?
        # TODO: output music

    print("Finished")

    pass


def computeFitness(genNum, currGen):
    #TODO: compute fitness for first generation
    print("Computing Fitness for generation" + genNum)

def computeFitness(genNum, currGen, nextGen):
    print("Computing Fitness for generation" + genNum)

def selection(genNum, currGen, nextGen):
    print("Selecting best performers" + genNum)

def crossover(genNum, pocurrGenp, nextGen):
    print("Crossing over" + genNum)

def mutation(genNum, pocurrGenp, nextGen):
    print("Mutating" + genNum)


if __name__ == "__main__":
    main()


