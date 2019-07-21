
# coding: utf-8

# In[477]:


from random import *
import numpy as np


# In[478]:


def generatePopulation(popSize):
    #Generates population with chromosomes with 6 random numbers between 1 and 6 each
    population = []
    for i in range(popSize):
        gene = []
        for x in range(6):
            gene.append(randint(1,6))
        population.append(gene)
    return population


# In[479]:


def evaluateFitness(population):
    fitness = [0] * len(population)
    goal = [1,2,3,4,5,6]
    counter = 0
    #foreach correct position
    for i in population:
        for index in range(6):
            if i[index] == goal[index]:
                fitness[counter] += 1
    return fitness


# In[480]:


def evaluateFitness(population):
    fitness = [0] * len(population)
    counter = 0
    for i in population:
        if(i[0]==1):
            fitness[counter] += 1
        if(i[1]==2):
            fitness[counter] += 1
        if(i[2]==3):
            fitness[counter] += 1
        if(i[3]==4):
            fitness[counter] += 1
        if(i[4]==5):
            fitness[counter] += 1
        if(i[5]==6):
            fitness[counter] += 1
        counter += 1
    return fitness


# In[481]:


def breedChilds(population):
    new_population = []
    fitness = evaluateFitness(population)
    while(len(population)>1):
        #choose two best parents, remove them from the list, breed and reiterate      
        chromosome1 = population.pop(np.argmax(fitness))
        fitness.pop(np.argmax(fitness))
        chromosome2 = population.pop(np.argmax(fitness))
        fitness.pop(np.argmax(fitness))
        #breed
        child1, child2 = crossover(chromosome1, chromosome2)
        new_population.append(child1)
        new_population.append(child2)
    return new_population


# In[482]:


def crossover(gene1,gene2):
    crossoverPoint = randint(0,len(gene1)-1)
    #print("Old Genes:")
    #print(gene1)
    #print(gene2)
    gene1_new = gene1[0:crossoverPoint] + gene2[crossoverPoint:len(gene2)]
    gene2_new = gene2[0:crossoverPoint] + gene1[crossoverPoint:len(gene1)] 
    #print("New genes:")
    #print(gene1_new)
    #print(gene2_new)
    return(gene1_new, gene2_new)


# In[483]:


def mutate(gene, chance):
    if(randint(0,99)<=chance):
        mutationPosition = randint(0,len(gene)-1)
        gene[mutationPosition] = randint(1,len(gene)-1)
        #print("Mutation happened")
        #print(gene)
    return(gene)


# In[496]:


#Create population
population = generatePopulation(50)
#evaluate fitness
generations = 1
max_gens = 200
while(max(evaluateFitness(population))<6 and generations < max_gens):
    population = breedChilds(population)
    #mutate with 5 percent chance of mutation
    for chromosome in population:
        mutate(chromosome, 1)
    generations += 1
    print("Generation: " + str(generations))
if(generations==max_gens):
    print("Cancel conditions met")
if(max(evaluateFitness(population))==6):
    print("EA successfull!")
    fitness = evaluateFitness(population)
    print("Index: " + str(np.argmax(fitness)) + " was successfull.")
    print(population[np.argmax(fitness)])

