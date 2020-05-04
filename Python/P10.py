
# Solution to problem 10
# https://projecteuler.net/problem=10
# Run time  5267.07ms

lst=[1]*3000000
num=2
for i in range(3,2000000,2):
    if i%2==0:
        continue
    elif lst[i]!=0:
        num+=i
    for j in range(2,(2000000//i)+1): # increace the lst length to avoid on one side i*j>lst.len
                                      # on the other hand to be able to trim j==2
            lst[(i*j)]=0

print(num)
# Answer: 142913828922
