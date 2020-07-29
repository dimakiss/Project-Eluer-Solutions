
# Solution to problem 65
# https://projecteuler.net/problem=65
# Run time 0 ms


n=100

#skiping the first number (2)
n-=1

#Create lst lst(e)=[2;1,2,1,1,4,..,1,2k,1]
lst=[]
for i in range(n):
    if i%3==1:
        lst.append(2*((i//3)+1)) # ...,1,2i,1.. format
    else:
        lst.append(1)
        
        
numerator=0
denominator=1
lst.reverse()
for i in lst:
    numerator+= i * denominator
    numerator, denominator= denominator, numerator


#Adding 2
numerator= numerator + 2 * denominator

#Sum all digits
sum_of_dig=0
for i in str(numerator):
    sum_of_dig+=int(i)
print(sum_of_dig)

# Answer: 272
