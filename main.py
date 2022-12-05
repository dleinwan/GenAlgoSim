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

import random

class Organism:
    genes = []
    fitness = 0

    def __init__(self):
        #TODO: randomize fitness
        self.fitness = random.randrange(1,100)
        #TODO: randomize genes
        #
        #example
        randomNum = random.randrange(1,100)
        self.genes = [randomNum]

        pass

# Population is made up of organisms
class Population:
    organisms = []
    #TODO: decide on population size
    size = 200 #make sure divisible by 4

    def __init__(self):
        for i in range(self.size):
            self.organisms.append(Organism())
        pass

def main():
    #TODO: decide on number of generations to run for
    #number of generations algorithm will run for
    numGens = 5

    print("Beginning of Generations")
    currGeneration = Population()

    #TODO: compute fitness
    computeFitness(1, currGeneration, currGeneration)

    printFitness(1, currGeneration)

    for genNum in range(1, numGens + 1):
        # STORE NEW DATA HERE
        nextGeneration = Population()
        print(genNum)

        #TODO: selection (kill off one half)
        selection(genNum, currGeneration, nextGeneration)

        printFitness(genNum, currGeneration)

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


def computeFitness(genNum, currGen, nextGen):
    print("Computing Fitness for generation " + str(genNum))
    #
    #example
    for organism in currGen.organisms:
        organism.fitness = organism.genes[0] % random.randrange(1,50) #random number to mod by 
        #print("fit: " + str(organism.fitness))
        # note: if your fitness calculation is the exact same every time, convergence will happen very quickly
    pass
    

def selection(genNum, currGen, nextGen):
    print("Selecting best performers " + str(genNum))
    #
    #example
    currGen.organisms.sort(key=lambda x: x.fitness, reverse=False) #sort population list by fitness
    pass

def crossover(genNum, currGen, nextGen):
    print("Crossing over " + str(genNum))
    #
    #example: the top 75-100 percentile and 50-75 percentile make two children each
    orgPerP = currGen.size / 4  #organisms per 25th percentile
    for parOne in range(int((currGen.size * 3/4)) - 1, currGen.size):
        # if size=200, parOne (first parent) from 149-199
        parTwo = parOne - 50  #parent two index
        #if size=200, replace lowest 100 with children of parents
        childOne = parOne - 199
        childTwo = parOne - 198
        currGen.organisms[childOne].genes[0] = currGen.organisms[parOne].genes[0] + currGen.organisms[parTwo].genes[0]
        currGen.organisms[childTwo].genes[0] = currGen.organisms[parOne].genes[0] - currGen.organisms[parTwo].genes[0]
    pass


def mutation(genNum, currGen, nextGen):
    print("Mutating " + str(genNum))
    pass


def printFitness(genNum, currGen):
    for organism in currGen.organisms:
        print(organism.fitness)


if __name__ == "__main__":
    main()


