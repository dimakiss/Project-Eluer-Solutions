# Solution to problem 2
# https://projecteuler.net/problem=2
# Run time less then 1ms


# sum_of_Fibonacci get n as the number
# sum_of_Fibonacci return the sum of even Fibonacci numbers below n
def sum_of_Fibonacci(n):
    n1,n2,n3=0,1,1
    sum=0
    while n3<n: #calculate the next Fibonacci numbers by the fromula Fn=Fn-1 + Fn-2 when Fn=n3 ; Fn-1=n2 ; Fn-2=n1
        n3=n1+n2
        n1=n2
        n2=n3
        if n2%2==0:
            sum+=n3
    return sum

print(sum_of_Fibonacci(4000000))
#Answer: 4613732
