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
        #TODO: randomize fitness
        self.midi = random.randrange(1, 50)
        #TODO: randomize genes
        #
        #example
        randomNum = random.randrange(1, 50)
        self.genes = [randomNum]
        pass

class Population:
    organisms = []
    #TODO: decide on population size
    size = 60 #make sure divisible by 4

    def __init__(self):
        self.organisms = []
        self.size = 60
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
        # printFitnessOneLine(genNum, currGeneration)
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
        while n <= 127:
            base_notes.append(n)
            n += 12
    return base_notes

def computeFitness(genNum, currGen):
    #print("Computing Fitness for generation " + str(genNum))
    base_midi = random.randrange(1, 11)
    arp_notes = genArpeggioMap(base_midi)
    for organism in currGen.organisms:
        organism.fitness = 1 if organism.midi in arp_notes else 0
        # print (f'Organism fitness: {organism.fitness}')
        # randNum = random.randrange(1, 200)
        # organism.fitness = min(organism.genes[0] % randNum, 10) #random number to mod by 
        # print(f'Type(Organism) genes: {organism.genes[0]}, fit:  {str(organism.fitness)}, randNum: {randNum}')
        # note: if your fitness calculation is the exact same every time, convergence will happen very quickly
    pass
    

def selection(genNum, currGen):
    #print("Selecting best performers " + str(genNum))
    
    # Sort array by fitness and midi value with lowest value first.
    # Retrieve organisms with fitness == 1
    fitness_array = [org.fitness for org in currGen.organisms]
    midi_array = [org.midi for org in currGen.organisms]
    orgs = [org for org in currGen.organisms]
    matrix = zip(fitness_array, midi_array, orgs)
    # [print (t) for t in list(matrix)]
    matrix = sorted(matrix, key=lambda x: (x[0], x[1]), reverse=False)
    # Extract a list containing all organism objects in test
    currGen.organisms = [t[2] for t in matrix]

    # [print (f'prev: {org.midi}') for org in currGen.organisms]
    # currGen.organisms.sort(key=lambda x: x.fitness, reverse=False) #sort population list by fitness
    # [print (f'post: {org.midi}') for org in currGen.organisms]
    # print (f'Number of organisms post selection: {len(currGen.organisms)}')
    pass

def crossover(genNum, currGen):
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
        currGen.organisms[childOne].genes[0] = (currGen.organisms[parOne].genes[0] + currGen.organisms[parTwo].genes[0]) % (currGen.size/2)
        currGen.organisms[childTwo].genes[0] = (currGen.organisms[parOne].genes[0] + currGen.organisms[parTwo].genes[0]) % (currGen.size/4)
        pass
    print (f'Number of organisms post crossover: {len(currGen.organisms)}')
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
    # print  (genNum)
    for organism in currGen.organisms:
        playing = 1
        client.send_message("playing", playing)
        i = i + 1
        #if (i % 2):
        print (f'playing: {organism.midi}')
        client.send_message("midi", organism.midi)
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




