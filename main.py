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

#################################################################################################################

import random
import matplotlib.pyplot as plt
import time
import argparse

from pythonosc import udp_client


#################################################################################################################
# CLASSES

class Organism:
    genes = []
    fitness = 0

    def __init__(self, size):
        #TODO: randomize fitness
        self.fitness = random.randrange(1, 5)
        #TODO: randomize genes
        #
        #example
        randomNum = random.randrange(1, 10)
        self.genes = [randomNum]
        pass

class Population:
    organisms = []
    #TODO: decide on population size
    size = 200 #make sure divisible by 4

    def __init__(self):
        self.organisms = []
        self. size = 200
        for i in range(self.size):
            self.organisms.append(Organism(self.size))
        pass



#################################################################################################################
# MAIN

def main():
    #TODO: decide on number of generations to run for
    #number of generations algorithm will run for
    numGens = 10

    print("Beginning of Generations")
    currGeneration = Population()

    #TODO: compute fitness
    computeFitness(0, currGeneration)

    printFitness(0, currGeneration)
    plotFitness(0, currGeneration)

    for genNum in range(1, numGens + 1):
        print(genNum)

        #TODO: selection (kill off one half)
        selection(genNum, currGeneration)

        #TODO: crossover (reproduce)
        crossover(genNum, currGeneration)

        #TODO: mutate
        mutation(genNum, currGeneration)

        computeFitness(genNum, currGeneration)

        # show fitness
        findAvgFitness(genNum, currGeneration)
        plotFitness(genNum, currGeneration)
        #play midi

        # wait until last generation's music is done?
        # TODO: output music
        # use currGeneration.organisms[i].fitness as MIDI notes

        pass

    print("Finished")

    pass

#################################################################################################################
# FUNCTIONS


def computeFitness(genNum, currGen):
    #print("Computing Fitness for generation " + str(genNum))
    #
    #example
    for organism in currGen.organisms:
        organism.fitness = organism.genes[0] % random.randrange(1,50) #random number to mod by 
        #print("fit: " + str(organism.fitness))
        # note: if your fitness calculation is the exact same every time, convergence will happen very quickly
    pass
    

def selection(genNum, currGen):
    #print("Selecting best performers " + str(genNum))
    #
    #example
    currGen.organisms.sort(key=lambda x: x.fitness, reverse=False) #sort population list by fitness
    pass

def crossover(genNum, currGen):
    #print("Crossing over " + str(genNum))
    #
    #example: the top 75-100 percentile and 50-75 percentile make two children each
    orgPerP = currGen.size / 4  #organisms per 25th percentile
    for parOne in range(int((currGen.size * 3/4)) - 1, currGen.size):
        # if size=200, parOne (first parent) from 149-199
        parTwo = parOne - 50  #parent two index
        #if size=200, replace lowest 100 with children of parents
        childOne = parOne - 199
        childTwo = parOne - 198
        currGen.organisms[childOne].genes[0] = (currGen.organisms[parOne].genes[0] + currGen.organisms[parTwo].genes[0]) % (currGen.size/2)
        currGen.organisms[childTwo].genes[0] = (currGen.organisms[parOne].genes[0] + currGen.organisms[parTwo].genes[0]) % (currGen.size/4)
        pass
    pass


def mutation(genNum, currGen):
    #print("Mutating " + str(genNum))
    numMutated = currGen.size / 2
    for i in range(1, int(numMutated)):
        randomNum = random.randrange(0, currGen.size)
        currGen.organisms[randomNum].genes[0] = random.randrange(1, int(currGen.size/2))
        pass
    pass

def printFitness(genNum, currGen):
    for organism in currGen.organisms:
        print(organism.fitness)
    pass

def plotFitness(genNum, currGen):
    x = []
    y = []
    i = 0
    for organism in currGen.organisms:
        i = i + 1
        x.append(i)
        y.append(organism.genes[0])
        pass
    plt.plot(x, y)
    plt.xlabel('Organism n')
    plt.ylabel('Fitness')
    plt.title('Fitness for Generation ' + str(genNum))
    plt.show()
    pass

def findAvgFitness(genNum, currGen):
    total = 0
    for organism in currGen.organisms:
        total = total + organism.genes[0]
    avgFitness = total / currGen.size
    print("Gen " + str(genNum) + " Avg Fit: " + str(avgFitness))


#################################################################################################################

if __name__ == "__main__":
    main()



