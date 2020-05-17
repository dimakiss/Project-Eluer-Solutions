
#Solution to problem 29
#https://projecteuler.net/problem=29
#Run time 678.39ms

lst=[]
for a in range(2,101):
    for b in range(2,101):
        temp=a**b
        if temp not in lst:
            lst.append(temp)

print(lst.__len__())
#Answer: 9183
