
# Solution to problem 69
# https://projecteuler.net/problem=69
# Run time  73599.58 ms

#Eulers_totient_function get num as the number 
#Eulers_totient_function return the totient value of the number ----> see in wikipedia for more deeper understanding
def Eulers_totient_function(num):
    up=num
    low=1
    if num%2==0:
        up *= 1
        low *= 2
        while num%2==0:
            num//=2
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            up*=(i-1)
            low*=i
        while num%i==0:
            num//=i
    if num!=0 and num!=1:
        up*=num-1
        low*=num
    return (up/low)

max1=0
index=0
for i in range(7,1000000):
    n_over_totient_of_i=i/Eulers_totient_function(i)
    if max1<n_over_totient_of_i:
        index=i
        max1=n_over_totient_of_i
print(max1,index)
# Answer: 510510
