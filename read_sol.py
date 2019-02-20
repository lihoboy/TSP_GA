file=open("bays29_sol","r")
list=[]
for i in (file):
    list.append(i)
for i in range(len(list)):
    list[i]=int(list[i])-1
print(list)