
# Solution to problem 72
# https://projecteuler.net/problem=72
# Run time 46640 ms


#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True


def prime_factors(num):
    prime_fact=[]
    if num%2==0:
        prime_fact.append(2)
        while num%2==0:
            num/=2
    for i in range(3,int(math.sqrt(num))+1,2):
        if num%i==0:
            prime_fact.append(i)
            while num % i== 0:
                num /= i
    if num!=1:
        prime_fact.append(num)
    return prime_fact

# find all numbers n that n/num is the most simplified version on the fraction
def totient(num):
    prime_fact=prime_factors(num)
    result1=num*1.0
    for i in prime_fact:
        result1*=pi[int(i)]
    return result1


num=1000000
count=0
pi=[0,0,0.5]
for i in range(3,num+1,2):
    pi.append(0)
    if is_prime(i):
        pi[-1]=(i-1)/i
    pi.append(0)


for i in range(2,num+1):
    count+=totient(i)
    #print(i)
print(count)
# Answer: 303963552391