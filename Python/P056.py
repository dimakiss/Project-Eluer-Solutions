
# Solution to problem 56
# https://projecteuler.net/problem=56
# Run time 1792.49ms


# sum every digits int the list of the broken number ( broken means broken to digits)
def sum(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum



max1=0
for a in range(2,100):
    print(a)
    lst = [0] * (int(math.log10(a))+1)*99 #list of the number a^b broken to digits
    lst[-1]=1
    temp=0
    for b in range(1,100): # calculate every a^b by multiplying a*a.. b times a summing every a^b in the process
                           #, for example, we u calculate 2^5 if u do first 2*2 then adding another 2 and again u will
                           # calculate 2^2 2^3 2^4 and finally 2^5

        for i in range(lst.__len__()-1,1,-1):
            lst[i]=lst[i]*a+temp%10
            temp=temp//10 +lst[i]//10
            lst[i]%=10
        max1=max(max1,sum(lst))
print(max1)
# Answer: 972
