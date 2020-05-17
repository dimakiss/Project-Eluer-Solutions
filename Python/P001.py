#Solution to problem 1 
#https://projecteuler.net/problem=1
#Run time 1ms


#find_sum get n as the number
#find_sum returns the sum of numbers below n which are multiples of 3 or 5
def find_sum(n):
    sum=0
    for i in range(n):
        if i%3==0 or i%5==0:
            sum+=i
    return sum
print(find_sum(1000))
#Answer: 233168
