
# Solution to problem 37
# https://projecteuler.net/problem=37
# Run time  4216.16 ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
    
#truncatable gets num as the number
#truncatable returns if the nuymber is truncatable from left to right and right to left
def truncatable(num):
    index=1
    while index<str(num).__len__():
        if is_prime(int(str(num)[index:])) and is_prime(int(str(num)[:-index])):
            index+=1
        else:
            return False
    return True

i=10 #2,3,5,7 not included 
count=0
sum=0
while count!=11: # we know there are 11 of them
    if is_prime(i) and truncatable(i):
        count+=1
        sum+=i
        print(i,count,sum)
    i+=1
# Answer: 872187
