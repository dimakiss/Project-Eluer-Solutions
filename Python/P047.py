
# Solution to problem 47
# https://projecteuler.net/problem=47
# Run time 943 ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

def dif_div(num):

    # test if there are 4 different prime divisors
    # the then a*b*c*d=number the largest d possible if a=2 b=3 c=5 so 30*d=numer
    # we need to check only until the square of the number
    count=0
    for i in range(2,int((num//30)**0.5)+1):
        if num%i==0:
            count+=1
            if count>4:
                return False
            while num%i==0:
                num//=i
    return count==4 or (count==3 and  is_prime(num))


num=15
count=0
while count!=4:

    if dif_div(num):
        count+=1
    else:
        count=0
    num+=1
print(num-4)
#Answer: 134043
