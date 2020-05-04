
# Solution to problem 12
# https://projecteuler.net/problem=12
# Run time  7819.57 ms

#divisitors get num as the number
#divisitors return the number of divisors of num
def divisitors(num):
    count=2
    sqrt=int(num**0.5)
    for i in range(2,sqrt):
        if num%i==0:
            count+=2
    if int(sqrt)**2==num:
        count+=1
    return count
num=3
counter=3
while divisitors(num)<500:
    num+=counter
    counter+=1
print(num)
# Answer: 76576500
