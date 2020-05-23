
# Solution to problem 87
# https://projecteuler.net/problem=87
# Run time  1430.67 ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

primes=[]
pows=[]
cubes=[]
qouad=[]

# calculating all the pows,cubes and quads and store them
for i in range(2,7073):
    if is_prime(i):
        primes.append(i)
        if i<=7071:     #x^2-50000000-2^3-2^4 ==>x=7071
            pows.append(i**2)
        if i<=368:      #x^3-50000000-2^2-2^4 ==>x=368
            cubes.append(i**3)
        if i<=84:   #x^2-50000000-2^3-2^4 ==>x=84
            qouad.append(i**4)
numbers=[]
lst=[0]*50000000 # all number form 0 to 50 mill
count=0
# brute force 7071*368*84
for a in qouad:
    for b in cubes:
            if a+b>49999998:
                break
            for c in pows:
                if a+b+c<50000000 and lst[a+b+c]==0:
                    lst[a+b+c]=1
                    count+=1
print(count)
# Answer: 1097343
