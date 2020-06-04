
# Solution to problem 44
# https://projecteuler.net/problem=44
# Run time 2162 ms

# if num in sires so 2k=3n^2-n
# so n= (1+sqrt(1-24k))/6 so we will check if (1+sqrt(1-24k))%6.0==0 also checking if its int or float
def is_pen(num):
    det=math.sqrt(1+24*num)+1
    return det%6.0==0

found=False
i=0
lst=[]

while not found:
    i+=1
    n=i*(3*i-1)//2
    for j in lst:
        if is_pen(n-j) and is_pen(n+j) and not found:
            found=True
            print(n-j,j)
    lst.append(n)
