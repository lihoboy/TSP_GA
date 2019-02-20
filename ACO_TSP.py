import copy
import random
def main():
    ''''''
    '''------read file-----------'''
    # read file
    file = open("bays29.tsp", "r")
    #uy734 79114
    #berlin52 7542
    read_list = []

    # write in list
    for i in file:
        read_list.append(i.split(" "))
    file.close()

    # trans to float
    each_city = []
    dist_list = []
    # print(read_list)
    for i in range(len(read_list)):

        for j in range(len(read_list[i])):
            if read_list[i][j] != "" and read_list[i][j] != "\n":
                # print(read_list[i][j])
                # read_list[i][j] = read_list[i][j].replace('\n','')
                read_list[i][j] = float(read_list[i][j])
                each_city.append(read_list[i][j])

        dist_list.append(each_city)
        each_city = []
    # for i in range(len(dist_list)):
    #     print(dist_list[i])
    '''-----init global pheromone---------------'''
    opt = [0, 27, 5, 11, 8, 4, 25, 28, 2, 1, 19, 9, 3, 14, 17, 16, 13, 21, 10, 18, 24, 6, 22, 26, 7, 23, 15, 12, 20]
    '''---paremeter for refresh-----------------'''
    count_same_sol=0
    count_same_flag = 0
    temp_best=0

    pheromone_list=[]
    pheromone_update=[]
    list_init=[]
    for i in range(len(dist_list)):
        list_init.append(1)
    for i in range(len(dist_list)):
        pheromone_list.append(copy.deepcopy(list_init))

    pheromone_update=copy.deepcopy(pheromone_list)

    # print(pheromone_list)
    # print(pheromone_update)

    reset_zero(pheromone_update)
    # print(pheromone_list)
    # print(pheromone_update)
    '''-----init ants---------------'''
    num_ants=100
    num_round=1000000000
    alpha = 5
    beta = 1
    lo = 0.5
    init_seq_candidate=[]
    ant_list=[]
    for i in range(len(dist_list)):
        init_seq_candidate.append(i)
    # print(init_seq_candidate)

    for i in range(num_ants):
        init_ant=ant(init_seq_candidate[:])
        # print( init_ant.seq_candidate)
        init_ant.seq_done.append(init_ant.seq_candidate.pop(0))
        # print(init_ant.seq_candidate)
        # print( init_ant.seq_done)
        ant_list.append(init_ant)

    best_ant=ant(init_seq_candidate[:])
    best_ant.dist=99999999
    '''---run n round-----------'''
    #count_same_sol=0
    #count_same_flag=0
    for round in range(num_round):
        if temp_best==best_ant.dist:
            count_same_sol+=1
        else:
            temp_best=best_ant.dist
            count_same_sol=0
        if count_same_sol>=100:
            count_same_flag=1

        if(round%100==0):
            print("Round ",round,"\n dist= ",best_ant.dist,"\n seq=",best_ant.seq_done)

        '''---run each ant-------'''
        for each_ant in range(num_ants):
            if count_same_flag==1:
                count_same_flag=0
                # print("--before----------------------")
                # print(pheromone_list)
                '''---reset_one----------'''
                # reset_one(pheromone_list)

                # print("--after----------------------")
                # print(pheromone_list)
                # reset_one(pheromone_list)
                # print("reset")
                ant_choice = ant_list[each_ant]
                ant_choice.seq_done=best_ant.seq_done[:]
                # print(ant_choice.seq_done)
                continue

            '''ACO iteration for each ant '''
            ant_choice = ant_list[each_ant]
            while len(ant_choice.seq_candidate) > 1:
                p_list = []
                each_p = 0
                sum_p = 0
                # print(ant_choice.seq_done[-1])
                # print(ant_choice.seq_candidate[0])
                # print(dist_list[ant_choice.seq_done[-1]][ant_choice.seq_candidate[0]])
                for i in range(len(ant_choice.seq_candidate)):
                    # dist_choice.append(1/dist_list[ant_choice.seq_done[-1]][ant_choice.seq_candidate[i]])
                    # pheromone_choice.append(pheromone_list[ant_choice.seq_done[-1]][ant_choice.seq_candidate[i]])
                    # print(ant_choice.seq_done[-1])
                    # print(dist_list[ant_choice.seq_done[-1]][ant_choice.seq_candidate[i]])
                    each_p = pow(1 / dist_list[ant_choice.seq_done[-1]][ant_choice.seq_candidate[i]], alpha) * pow(
                        pheromone_list[ant_choice.seq_done[-1]][ant_choice.seq_candidate[i]], beta)
                    p_list.append(each_p)
                    sum_p += each_p
                choose_next = random.choices(ant_choice.seq_candidate, p_list, k=1)
                ant_choice.seq_candidate = [x for x in ant_choice.seq_candidate if x != choose_next[0]]
                ant_choice.seq_done.append(choose_next[0])
                # print(choose_next)

            # pop last one
            ant_choice.seq_done.append(ant_choice.seq_candidate.pop(0))
            # print(choose_next)
            ant_choice.dist = count_dist(dist_list, ant_choice.seq_done)
            if best_ant.dist>ant_choice.dist:
                best_ant.dist=ant_choice.dist
                best_ant.seq_done=ant_choice.seq_done[:]
                # print("Update",best_ant.dist)
            # print(ant_choice.seq_done)
            # print(ant_choice.seq_candidate)
            # print(ant_choice.dist)
        '''after each ant done update pheromone '''
        sum_all_dist = 0
        dist_sum = 0
        for i in range(len(ant_list)):
            dist_sum += ant_list[i].dist
        # print()
        for i in range(len(ant_list)):
            for j in range(len(ant_list[i].seq_done)):
                if j == len(ant_list[i].seq_done) - 1:
                    pheromone_update[ant_list[i].seq_done[j]][ant_list[i].seq_done[0]] +=  ant_list[
                        i].dist / dist_sum
                else:
                    pheromone_update[ant_list[i].seq_done[j]][ant_list[i].seq_done[j + 1]] +=  ant_list[
                        i].dist / dist_sum
        for i in range(len(pheromone_list)):
            for i in range(len(pheromone_list[i])):
                pheromone_list[i][j] *= lo
                pheromone_list[i][j] += pheromone_update[i][j]
        reset_zero(pheromone_update)
        for i in range(num_ants):
            # print(i)
            ant_list[i].seq_done = []
            ant_list[i].seq_candidate= init_seq_candidate[:]
            ant_list[i].dist=999999
            ant_list[i].seq_done.append(ant_list[i].seq_candidate.pop(0))







    #
    # print(dist_choice)
    # print(pow(2, 3))
    # print(p_list)


class ant():
    def __init__(self,seq_candidate):
        self.dist=0
        self.seq_done=[]
        self.seq_candidate=seq_candidate
    # def __repr__(self):
    #     print(self.dist)

def reset_zero(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            list[i][j]=0
def reset_one(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            list[i][j]=2-list[i][j]

def count_dist(dist_list,sequence):
    count_dist=0
    for i in range (len(sequence)):
        if i==len(sequence)-1 :
            count_dist += dist_list[sequence[i]][sequence[0]]
        else:
            count_dist+=dist_list[sequence[i]][sequence[i+1]]

    return count_dist





if __name__ == "__main__":
    # execute only if run as a script
    main()