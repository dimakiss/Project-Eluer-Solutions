
#Solution to problem 21
#https://projecteuler.net/problem=21
#Run time 136.96ms

#divisitors get num as the number
#divisitors return the number of divisors of num
def divisitors_sum(num):
    sum=1
    sqrt=int(num**0.5)
    for i in range(2,sqrt):
        if num%i==0:
            sum+=i+num//i
    if int(sqrt**2)==num:
        sum+=int(sqrt)
    return sum

sum=0
for i in range(3,10000):
    temp=divisitors_sum(i)
    if divisitors_sum(temp)==i and temp!=i:
        sum+=i+temp
print(sum//2) # its take twice every option for example in i==220  d(220) = 284 it will tkae 220 284 and for i==284 the same
#Answer: 31626
