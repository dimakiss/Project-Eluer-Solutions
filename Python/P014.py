
# Solution to problem 134
# https://projecteuler.net/problem=14
# Run time  4809.25 ms

lst=[0]*1000000 # holder of the length of every number's chain
max1=0
for i in range(1,lst.__len__()):
    num=i
    counter=1
    while num!=1:
        counter+=1
        if num%2==0:
            num//=2
        else:
            num=num*3+1
        if lst.__len__()>num and lst[num]!=0: #if already check from current num and on...
            counter+=lst[num]
            num=1
            break
    lst[i]=counter
    if lst[max1]<lst[i]:
        max1=i
    count=0

print(max1)
# Answer: 837799
