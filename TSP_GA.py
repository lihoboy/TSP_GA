import numpy as np
import random
import copy
def main():
    ''''''
    '''------read file-----------'''
    # read file
    file = open("bays29.tsp", "r")
    read_list = []

    # write in list
    for i in file:
        read_list.append(i.split(" "))
    file.close()

    # trans to float
    each_city=[]
    dist_list=[]
    for i in range(len(read_list)):
        for j in range(len(read_list[i])):
            if read_list[i][j]!="" :
                read_list[i][j] = float(read_list[i][j])
                each_city.append(read_list[i][j])
        dist_list.append(each_city)
        each_city = []
    '''----------init population------------'''
    num_cities=len(read_list)
    population_list=[]
    individual=[]
    best_dist=999999999
    best_node=node_individual(best_dist,[])
    num_individual=1000
    '''--------init sample individual------'''
    for i in range(len(dist_list)):
        individual.append(i)
    #print(individual)
    for i in range (num_individual):
        generate_individual=np.random.permutation(individual)
        generate_individual=nparray_to_list(generate_individual)
        node_init=node_individual(count_dist(dist_list,generate_individual),generate_individual)
        population_list.append(node_init)
        if node_init.dist <best_node.dist:
            best_node=node_init
    '''----------print population_list-----------------'''
    # for i in range(len(population_list)):
    #     print(population_list[i].fitness)
    #     print(population_list[i].seq)
    opt=[0, 27, 5, 11, 8, 4, 25, 28, 2, 1, 19, 9, 3, 14, 17, 16, 13, 21, 10, 18, 24, 6, 22, 26, 7, 23, 15, 12, 20]
    print(opt)
    print(count_dist(dist_list,opt))
    for generation in range(16000):

        if generation%200==0:
            print ("generation ",generation)
            print("best dist: ", best_node.dist, "\nseq : ", best_node.seq)
        '''----------GA iteration-------------------------'''

        '''---------crossover--------------------'''
        len_for_crossover=len(population_list)-1
        for i in range(0, len(population_list) - 1):
            seq_for_init=[]
            seq_for_init=crossover(num_cities, population_list[i].seq, population_list[random.randrange(len_for_crossover)].seq)
            node_init = node_individual(count_dist(dist_list, seq_for_init),seq_for_init)
            if node_init.dist < best_node.dist:
                best_node = node_init
                # print("best dist: ", best_node.dist, "\nseq : ", best_node.seq)
            population_list.append(node_init)
        # print("len(population_list)", len(population_list))
        '''-------mutation---------------------'''
        population_list = sorted(population_list, key=lambda x: x.dist)
        # for i in range(len(population_list)):
        #     print(population_list[i].dist)
        for i in range(int(len(population_list)/2), int(len(population_list) / 50), -1):

            if random.random() < 0.9:
                generate_individual = np.random.permutation(individual)
                generate_individual = nparray_to_list(generate_individual)
                node_init = node_individual(count_dist(dist_list, generate_individual), generate_individual)
                population_list.pop(i)
                population_list.insert(i,node_init)
                if node_init.dist < best_node.dist:
                    best_node = node_init
                    # print("best dist: ", best_node.dist, "\nseq : ", best_node.seq)
        # print("len(population_list)", len(population_list))
        '''-----selection----------------------'''
        fitness_list = []
        fitness_sum = 0
        # print(type(population_list[0].dist))
        for i in range(0, len(population_list)):
            fit = 1 / population_list[i].dist
            fitness_sum += fit
            fitness_list.append(fit)

        population_list = random.choices(population_list, fitness_list, k=num_individual)
        # print("len(population_list)", len(population_list))



    '''-------print global best sol---------------------'''
    print("best dist: ",best_node.dist,"\nseq : ",best_node.seq)



def count_dist(dist_list,sequence):
    count_dist=0
    for i in range (len(sequence)):
        if i==len(sequence)-1 :
            count_dist += dist_list[sequence[i]][sequence[0]]
        else:
            count_dist+=dist_list[sequence[i]][sequence[i+1]]

    return count_dist

class node_individual():
    def __init__(self, dist, seq):

        self.fitness = 0
        self.seq = seq
        self.dist = dist

def crossover(num_cities,seq1,seq2):
    # num_cities = 10
    seq1_c=copy.copy(seq1)
    seq2_c=copy.copy(seq2)
    left=random.randrange(num_cities)
    right=random.randrange(num_cities)
    if left>right:
        tmp=left
        left=right
        right=tmp
    # left=3
    # right=5
    # print(left," ",right)
    # for i in range(100):
    #     print(random.randrange(num_cities))
    # print("1",seq1)
    # print("2",seq2)
    for i in range(left,right+1):
        seq2_c.remove(seq1_c[i])
    for i in range(left, right + 1):
        seq2_c.insert(i,seq1_c[i])
    # print(seq1)
    # print(seq2)
    return seq2_c

def nparray_to_list(seq):
    list=[]
    # print("seq",seq)
    for i in range (len(seq)):
        list.append(seq[i])
    # print("list",list)
    return list






if __name__ == "__main__":
    # execute only if run as a script
    main()