'''
bays29 : 2020
berlin52 : 7542
'''
def count_dist(delta_x,delta_y):
    delta_x*=delta_x
    delta_y *= delta_y

    return (delta_x+delta_y)**0.5

#read file
file=open("berlin.tsp","r")
read_list=[]

#write in list
for i in file:
    read_list.append(i.split(" "))
file.close()
#trans to float
for i in range(len(read_list)):
    for j in range(len(read_list[0])):
        read_list[i][j] = float(read_list[i][j])

#count distance
output_list = []
each_city = []
dist=0
for i in range(len(read_list)):
    x=read_list[i][1]
    y=read_list[i][2]
    for j in range(len(read_list)):
        x_other = read_list[j][1]
        y_other = read_list[j][2]
        dist=count_dist(x-x_other,y-y_other)
        each_city.append(dist)
    output_list.append(each_city)
    each_city=[]



# for i in range(len(read_list)):
#     print(i)


# print (output_list)
#Write file
print("Writing")
f_w=open("berlin52.tsp","w")
for i in range(len(output_list)):
    print("line ",i)
    for j in range(len(output_list[0])):
        f_w.write("%.0f"%(output_list[i][j]))
        f_w.write(" ")
    f_w.write("\n")