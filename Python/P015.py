
# Solution to problem 15
# https://projecteuler.net/problem=15
# Run time 0.65 ms

n=21
lst=[]

# In every point the NxN grid there is only 2 option down or right,
# so if we go backward from the end when the end is 1
# every point is the sup of the point on its right and downside
# This algorithm runs row by row 
for i in range(n):
    temp=[]
    for j in range(n):
        if(i==n-1 or j==n-1):
            temp.append(1)
        else:
            temp.append(0)

    lst.append(temp)


for i in range(n-2,-1,-1):
    for j in range(n-2,-1,-1):
        lst[i][j]+=lst[i+1][j]+lst[i][j+1]

print(lst[0][0])
# Answer: 137846528820
