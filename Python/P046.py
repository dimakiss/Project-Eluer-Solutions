
# Solution to problem 46
# https://projecteuler.net/problem=46
# Run time 1707 ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True


# generate 1000 primes
primes=[]
number=2
while primes.__len__()<1000:
    if is_prime(number):
        primes.append(number)
    number+=1
number=9
found=True
while found:
    found=False

    for i in range(0,int((number)**0.5)+1):
        if (number-2*(i**2)) in primes:
            found=True
            break

    if found==False: # if not found
        break

    # else

    found=True
    number+=2
print(number)
#Answer: 5777
