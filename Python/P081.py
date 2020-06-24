
# Solution to problem 81 
# https://projecteuler.net/problem=81
# Run time 9 ms

#lst=[[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[637,699,497,121,956],[805,732,524,37,331]]
lst=[]

with open('matrix.txt','r') as f:
    buff=f.read()
for i in buff.split('\n'):
    temp=[]
    for j in i.split(','):
        temp.append(int(j))
    lst.append(temp)

# initiating the lowest and rightest position
for i in range(lst.__len__()-2,-1,-1):
    lst[i][lst.__len__()-1]+=lst[i+1][lst.__len__()-1]
for i in range(lst.__len__()-2,-1,-1):
    lst[lst.__len__()-1][i]+=lst[lst.__len__()-1][i+1]

# by going from the end, in every position, there is an option to go right or down
for i in range(lst.__len__()-2, -1, -1):
    for j in range(lst.__len__()-2, -1, -1):
           lst[i][j]+=min(lst[i][j+1],lst[i+1][j])
print(lst[0][0])
#Answer: 427337
