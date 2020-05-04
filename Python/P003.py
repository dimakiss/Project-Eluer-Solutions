
# Solution to problem 3
# https://projecteuler.net/problem=3
# Run time less then 1ms

#To solve this problem we will mention that every number can be represented by its prime factor
#for example 81=3^4 ; 85=17*5 ;1050=2*3*5^2 *7
#the first number the divide 1050, for example, is 2 we will be divided 1050 by to and we will get 525
#525 divided by 3 we will get 175 which divided by 5 twice and we left with 7 which indeed the largest prime factor
 
# calculate get n as the number
# calculate return the Largest prime factor
def calculate(n):
        p=2
        while True:
            p = smallest_prime_factor(n,p)
            if n==p:
                return n
            n //=p
        return 0

# smallest_prime_factor get n as number and k as last know number that divides n 
#(by default this number as smallest prime is 2)
#
# smallest_prime_factor return the smallest number that divides n
def smallest_prime_factor(n,k):
    for i in range(k, (int)(n**0.5) + 1):
        if n % i == 0:
            return i
    return n  # n itself is prime


print(calculate(600851475143 ))
# Answer: 6857
