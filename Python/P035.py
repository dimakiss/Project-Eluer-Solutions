
#Solution to problem 35
#https://projecteuler.net/problem=35
#Run time 3823.73ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

lst=[1]*1000000
count=1
def test(num):
    num=str(num)
    temp=num[1:]+num[0]
    while temp!=num :
        if lst[int(temp)]==0 or is_prime(int(temp))!=True:
            temp = num[1:] + num[0]
            while temp!=num and lst[int(temp)]!=0:
                lst[int(temp)] = 0
                temp = temp[1:] + temp[0]
            return False
        temp = temp[1:] + temp[0]
    return is_prime(int(num))
for i in range(3,lst.__len__(),2):
    if test(i):
        count+=1
print(count)
#Answer: 55
