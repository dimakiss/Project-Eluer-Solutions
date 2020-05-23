
# Solution to problem 50
# https://projecteuler.net/problem=50
# Run time  710.26 ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

sum=0
sum_p=[] # sum of all the primes till some n the prime
for i in range(2,100000):
    if sum+i>1000000:
        break
    elif is_prime(i):
        sum+=i
        sum_p.append(sum)

max1=0
for i in range(sum_p.__len__()): # if we won the sum of the primes from 6 to 9 we just subtract sum_p[9]-sum_p[6]=
                                 # the sum of all the primes from 6th prime to 9th prime and if its a
                                 # prime we check if its maximum prime sum
    for j in range(i):
        temp=sum_p[i]-sum_p[j]
        if is_prime(temp):
            max1=max(max1,temp)

print(max1)
# Answer: 997651
