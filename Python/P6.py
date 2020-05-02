# Solution to problem 6
# https://projecteuler.net/problem=6
# Run time 0.06ms


#sum_till_n get n as the number
#sum_till_n return the sum of the numbers from 1-n
def sum_till_n(n):
    return int((n+1)*(n/2))

sum_cubes=0
n=100
for i in range(n+1):
    sum_cubes+=i*i
sum_till=sum_till_n(n)

print(sum_till*sum_till-sum_cubes)
# Answer: 25164150
