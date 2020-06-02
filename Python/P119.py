
#Solution to problem 119
#https://projecteuler.net/problem=119
#Run time 289 ms

def digs_sum(str1):
    sum=0
    for i in str1:
        sum+=int(i)
    return sum

length=3
lst=[]
for i in range(2,100):
    for j in range(2,100):
        temp=str(i**j)
        if digs_sum(temp)==i:
            if temp not in lst:
                lst.append(temp)
lst.sort(key=len)

print(lst[29])
#Answer: 248155780267521
