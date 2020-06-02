
#Solution to problem 206
#https://projecteuler.net/problem=206
#Run time 39294 ms


def match(n):
    s = str(n)
    for i in range(8,-1,-1):
        if int(s[i*2])!=i+1:
            return False
    return True

n = 101010101 # sqrt(10203040506070809) 1020304050607080900 is mult of 100 so we took only 10203040506070809 as start
              # also 0 must be in the end 0 which must end with 00 because only multiple of 10
for i in range(n,10*n,2):
    if match(i*i):
        n=i
        break

print(n*10)
#Answer: 1389019170
