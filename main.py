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
import numpy as np

#from tkinter import *


from pythonosc import udp_client


#################################################################################################################
# CLASSES

class Organism:
    genes = []
    fitness = 0

    def __init__(self, size):
        
        #TODO: randomize genes
        #example
        midi = random.randrange(1, 50)
        self.genes = [midi]
        self.compute_init_fitness()
        pass

    def compute_init_fitness(self):
        arp_notes = genArpeggioMap(1)
        # print (f'self genes: {self.genes}, arp_notes: {arp_notes}')
        self.fitness = 1 if self.genes[0] in arp_notes else 0
        print (self.fitness)
        pass


class Population:
    organisms = []
    #TODO: decide on population size
    size = 200 #make sure divisible by 4

    def __init__(self):
        self.organisms = []
        self.size = 100
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
    numGens = 200

    print("Beginning of Generations")
    currGeneration = Population()

    #TODO: compute fitness
    computeFitness(0, currGeneration)

    # printFitnessOneLine(0, currGeneration)
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


def genArpeggioMap(midi):
    """
    Input base note to generate a M7 arpeggio map. ie, all notes across permissible octaves falling in the arpeggio
    """
    base_notes = [midi, midi + 4, midi + 7, midi + 10]
    for note in base_notes:
        n = note + 12
        while n <= 67:
            base_notes.append(n)
            n += 12
    return base_notes

def computeFitness(genNum, currGen, base_midi=1):
    #print("Computing Fitness for generation " + str(genNum))
    arp_notes = genArpeggioMap(base_midi)
    for organism in currGen.organisms:
        organism.fitness = 1 if organism.genes[0] in arp_notes else 0
    pass


def selection(genNum, currGen, base_midi=1):
    #print("Selecting best performers " + str(genNum))
    
    # Sort array by fitness and midi value with lowest value first.
    # Retrieve organisms with fitness == 1
    fitness_array = np.array([org.fitness for org in currGen.organisms])
    midi_array = np.array([org.genes[0] for org in currGen.organisms])
    orgs = np.array([org for org in currGen.organisms])
    ones_orgs = orgs[np.where(fitness_array == 1)[0]]
    zeros_orgs = orgs[np.where(fitness_array == 0)[0]]
    ones_midi = midi_array[np.where(fitness_array == 1)[0]]
    matrix = list(zip(ones_midi, ones_orgs))
    # print (f'prev: {matrix}')
    # [print (f'prev: {t[1]}, {t[0]}') for t in list(matrix)]
    matrix = sorted(matrix, key=lambda x: x[0], reverse=False)
    # print (matrix[0][1])
    currGen.organisms = [t[1] for t in matrix]
    # print (f'pre extended: {len(currGen.organisms)}')
    currGen.organisms.extend(list(zeros_orgs))
    # print (f'post extended: {len(currGen.organisms)}')

    pass


def crossover(genNum, currGen, base_midi=1):
    #print("Crossing over " + str(genNum))
    #
    #example: the top 75-100 percentile and 50-75 percentile make two children each
    orgPerP = currGen.size / 4  #organisms per 25th percentile
    for parOne in range(int((currGen.size * 3/4)) - 1, currGen.size):
        # if size=200, parOne (first parent) from 149-199
        parTwo = int(parOne - orgPerP)  #parent two index
        #if size=200, replace lowest 100 with children of parents
        childOne = int(parOne - (currGen.size - 1))
        childTwo = int(parOne - (currGen.size - 2))
        # print (f'parOne: {parOne}, parTwo: {parTwo}, childOne: {childOne}, childTwo: {childTwo}, len: {len(list(currGen.organisms))}')
        currGen.organisms[childOne].genes[0] = (currGen.organisms[parOne].genes[0] + currGen.organisms[parTwo].genes[0])//3 #% (currGen.size/2)
        currGen.organisms[childTwo].genes[0] = (currGen.organisms[parOne].genes[0] + currGen.organisms[parTwo].genes[0])//3 #% (currGen.size/4)
        currGen.organisms[childOne].fitness = 1 if currGen.organisms[childOne].genes[0] in genArpeggioMap(base_midi) else 0
        currGen.organisms[childTwo].fitness = 1 if currGen.organisms[childTwo].genes[0] in genArpeggioMap(base_midi) else 0
        pass
    print (f'Number of organisms post crossover: {len(currGen.organisms)}')
    pass


def mutation(genNum, currGen):
    #print("Mutating " + str(genNum))
    numMutated = currGen.size / 10
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
        print(f'{int(organism.fitness)}', end=' ')
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
    print(f'Gen {str(genNum)} Avg Fit: {str(avgFitness)}')

def playFitness(genNum, currGen):
    IP = "127.0.0.1"
    PORT_TO_MAX = 1001
    client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)

    playing = 0
    client.send_message("playing", playing)
    client.send_message("genNum", genNum)
    i = 0
    # print  (genNum)
    for organism in currGen.organisms:
        playing = 1
        client.send_message("playing", playing)
        i = i + 1
        #if (i % 2):
        # print (f'playing: {organism.genes}')
        client.send_message("midi", organism.genes[0])
        client.send_message("orgNum", i)
        time.sleep(.01)
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




