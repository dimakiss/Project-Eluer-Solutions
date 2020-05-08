
# Solution to problem 58
# https://projecteuler.net/problem=58
# Run time  5315.66 ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

# by some math we can see that the right diagonal is the square of odd number the spiral in subtraction
# i-1 whenever i is the number for example with 25 i=5 the first number is 25 -4=21 21-4=17
#17-4=13
counter=1
prime=0
index=1
while prime/counter>=0.1 or index<10:
    index+=2
    root=index*index
    p1=root-(index-1)
    p2 = root - 2*(index - 1)
    p3 = root - 3*(index - 1)
    if is_prime(p1):
        prime+=1
    if is_prime(p2):
        prime += 1
    if is_prime(p3):
        prime += 1
    counter+=4
print(index)
# Answer: 26241
