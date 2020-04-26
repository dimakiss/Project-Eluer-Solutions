Solution to problem 1 


#find_sum get n as number
#find_sum return the sum of numbers below n which are multiples of 3 or 5
def find_sum(n):
    sum=0
    for i in range(n):
        if i%3==0 or i%5==0:
            sum+=i
    return sum
print(find_sum(100000))
