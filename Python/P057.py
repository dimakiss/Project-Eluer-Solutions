
# Solution to problem 57
# https://projecteuler.net/problem=57
# Run time 288 ms

def convergents(n):

    #Checks if the numerator has more digits then the denominator

    n-=1
    lst=[]
    for i in range(n):
        lst.append(2)


    numerator=0
    denominator=1
    lst.reverse()
    for i in lst:
        numerator+= i * denominator
        numerator, denominator= denominator, numerator


    #Adding 1
    numerator+=denominator


    return len(str(numerator))>len(str(denominator))

count=0

for i in range(2,1001):
    if convergents(i):
        count+=1
        
print(count)
# Answer: 153
