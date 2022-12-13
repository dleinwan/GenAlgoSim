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

#from tkinter import *


from pythonosc import udp_client


#################################################################################################################
# CLASSES

class Organism:
    genes = []
    fitness = 0

    def __init__(self, size):
        #TODO: randomize fitness
        self.fitness = random.randrange(1, 2)
        #TODO: randomize genes
        #
        #example
        randomNum1 = random.randrange(1, 5)
        randomNum2 = random.randrange(1, 2)
        self.genes = [randomNum1, randomNum2]
        pass

class Population:
    organisms = []
    #TODO: decide on population size
    size = 200 #make sure divisible by 4

    def __init__(self):
        self.organisms = []
        self. size = 100
        for i in range(self.size):
            self.organisms.append(Organism(self.size))
        pass



#################################################################################################################
# MAIN

def main():

    # window = Tk()
    # window.title("ayyyyyeeeee")
    # lb = Label(window, text="ayyyeeee")
    # lb.place(x=15, y=21)
    # window.mainloop()


    #TODO: decide on number of generations to run for
    #number of generations algorithm will run for
    numGens = 2000

    print("Beginning of Generations")
    currGeneration = Population()

    #TODO: compute fitness
    computeFitness(0, currGeneration)

    printFitnessOneLine(0, currGeneration)
    playFitness(0, currGeneration)

    

    #plotFitness(0, currGeneration)

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
        printFitnessOneLine(genNum, currGeneration)
        #printFitnessOneLine(genNum, currGeneration)
        #plotFitness(genNum, currGeneration)

        # TODO: output music
        # using currGeneration.organisms[i].fitness as MIDI notes
        #play midi
        playFitness(genNum, currGeneration)
        # wait until last generation's music is done
        #input("press enter to continue")

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
        organism.fitness = organism.genes[0] % random.randrange(1,200) #random number to mod by 
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
        childOne = parOne - (currGen.size - 1)
        childTwo = parOne - (currGen.size - 2)
        # gene 1
        currGen.organisms[childOne].genes[0] = (currGen.organisms[parOne].genes[0] + currGen.organisms[parTwo].genes[0]) % (currGen.size/2)
        currGen.organisms[childTwo].genes[0] = (currGen.organisms[parOne].genes[0] + currGen.organisms[parTwo].genes[0]) % (currGen.size/4)

        computeFitness(genNum, currGen)
        # gene 2
        currGen.organisms[childOne].genes[1] = currGen.organisms[childOne].fitness + 14
        currGen.organisms[childTwo].genes[1] = currGen.organisms[childTwo].fitness + 14
        pass
    pass


def mutation(genNum, currGen):
    #print("Mutating " + str(genNum))
    numMutated = currGen.size / 25
    for i in range(1, int(numMutated)):
        randomNum = random.randrange(0, currGen.size)
        currGen.organisms[randomNum].genes[0] = random.randrange(1, int(currGen.size/2))
        pass
    pass

def printFitness(genNum, currGen):
    for organism in currGen.organisms:
        print(organism.fitness)
    pass

def printFitnessOneLine(genNum, currGen):
    for organism in currGen.organisms:
        print(int(organism.fitness), end=' ')
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

def playFitness(genNum, currGen):
    IP = "127.0.0.1"
    PORT_TO_MAX = 1001
    client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)

    playing = 0
    client.send_message("playing", playing)
    client.send_message("genNum", genNum)
    i = 0
    for organism in currGen.organisms:
        playing = 1
        client.send_message("playing", playing)
        i = i + 1
        #if (i % 2):
        client.send_message("midi", organism.fitness)
        client.send_message("midi2", organism.genes[1])
        client.send_message("orgNum", i)
        time.sleep(.05)
    playing = 0
    client.send_message("playing", playing)

def stopSound():
    IP = "127.0.0.1"
    PORT_TO_MAX = 1001
    client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)
    playing = 0
    client.send_message("playing", playing)

#################################################################################################################

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stopSound()
        print('Interrupted')




