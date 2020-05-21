
# Solution to problem 27
# https://projecteuler.net/problem=27
# Run time  5789.64 ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True


#The idea is simple we need to find a and b in the formula N^2+aN+b
#we will get a and b in the and as poss or negative
# they both cant be negative so only a can be changed
# if they both would be negative or especially b,
# we would get 0^2+0*a+b and if b<0, and n is always positive
# this number wouldn't be prime
# so only a can be negative



mxa1=0
a_max=0
b_max=0
for a in range(0,1000):
    for b in range(0,1000):
        countp=0
        countn=0
        bool_p=True # checks for positive if the mult of j**2-a*j+b was all the way prime
        bool_n=True # the same as bool_p
        j=0         # if they both were (not) primes we can stop because it's not consecutive
        while bool_n and bool_p:

            if bool_n and j**2-a*j+b<0 or is_prime(j**2-a*j+b)==False:
                bool_n =False
                if countn > mxa1:
                    a_max = -a
                    b_max = b
                    mxa1 = countn
            else:
                countn += 1
            if bool_p and j**2+a*j+b<0 or is_prime(j**2+a*j+b)==False:
                if countn > mxa1:
                    a_max = a
                    b_max = b
                    mxa1 = countn
            else:
                countp += 1
            j+=1
        if countn>mxa1:
            a_max=a
            b_max=b
            mxa1=countn
print(a_max,b_max,a_max*b_max)
# Answer: -59231
