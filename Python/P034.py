
# Solution to problem 34
# https://projecteuler.net/problem=34
# Run time 2281 ms

fact=[]
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)

def digfact(num):
    sum=0
    num=str(num)
    for i in num:
        sum+=fact[int(i)]
    return int(num)==sum

sum=0
for i in range(10):
    fact.append(factorial(i))
for i in range(3,fact[9]):
    if digfact(i):
        sum+=i
print(sum)
#Answer: 40730
