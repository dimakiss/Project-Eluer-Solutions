
# Solution to problem 23
# https://projecteuler.net/problem=23
# Run time 7606.66 ms

# give the sum of the elements in the list lst
def sum1(lst):
    counter_sum=0
    for i in lst:
        counter_sum+=i
    return counter_sum

# return list with divisors
def divisitors(num):
    lst=[1]
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            if num**0.5!=int(num**0.5) or int(num**0.5)!=i:
                lst.extend([num//i,i])
            else:
                lst.extend([num//i])
    return lst

lst=[]
non = [x for x in range(28123)] # all numbers till 28123
for i in range(12,28123):
    temp=divisitors(i)
    temp_sum=sum(temp)
    if temp_sum>i:
        lst.append(i)

for i in range(lst.__len__()):
    for j in range(i,lst.__len__()):
        if lst[i]+lst[j]<28123: # subtract all numbers that can be represented
            non[lst[i]+lst[j]]=0
        else:
            break

print(sum(non))
# Answer: 4179871
