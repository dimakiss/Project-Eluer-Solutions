
# Solution to problem 92
# https://projecteuler.net/problem=92
# Run time 35070.85ms


pow_list=[0]*10 #list of the powers from 1 to 9
# calculate the sum of the powered digits
def pows(num):
    sum=0
    while num>0:
        sum+=pow_list[num%10]
        num//=10
    return sum

lst=[0]*10000000
lst[89]=1
lst[1]=-1
temp=0
count=0
for i in range(10):
    pow_list[i]=i**2
for i in range(1,lst.__len__()):
    found=False
    temp=pows(i)
    templist=[i]
    while found==False:
        if lst[temp]!=0:
            for k in templist:# saving all the appearing sums in the way
                lst[k]=lst[temp]
            found=True
        else:
            templist.append(temp)
            temp=pows(temp)
    if lst[i] == 1:
        count += 1
print(count)
#Answer: 8581146
