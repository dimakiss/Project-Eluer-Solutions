
# Solution to problem 38
# https://projecteuler.net/problem=38
# Run time 1089 ms

def pandigital(num):
    lst=[]
    for i in num:
        if i not in lst:
            lst.append(i)
        else:
            return False
    return lst.__len__()==9 and "0" not in lst

max_num=0
# the max number to check is length 4 because if it was length 5 num*1 +num*2 (string adding) its was length 10 and
# we want a max 9
for i in range(1,10000):
    tempstr=""
    for j in range(1,int(9//int(math.log10(i*10))+1)): # we need that sum of num*j will be equal to 9 dig number
                                                       # so j can be larger then 9/(number's length)
        tempstr+=str(i*j)

    if pandigital(tempstr): # update
        max_num=max(int(tempstr),max_num)

print(max_num)
#Answer: 932718654
