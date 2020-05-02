
# Solution to problem 7
# https://projecteuler.net/problem=7
# Run time  256.4ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

prime_counter=2
number=3
while prime_counter<10001:
    number += 2
    if is_prime(number):
        prime_counter+=1

print(number)
# Answer: 104743
