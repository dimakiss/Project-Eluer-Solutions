
# Solution to problem 53
# https://projecteuler.net/problem=53
# Run time  111.37 ms


def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)



count=0
for n in range(1,101):
    for r in range(0,n):
        sum=1
        for i in range(r+1, n + 1): #n!=n*n-1 *...r*r-1*... n>r
            sum *= i                #n!/r!=n*n-1*..*r+1
        sum //= factorial(n - r)
        if sum>=1000000 :
            count+=1


print(count)
# Answer: 4075
