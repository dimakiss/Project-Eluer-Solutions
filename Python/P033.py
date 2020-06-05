
# Solution to problem 33
# https://projecteuler.net/problem=33
# Run time 1089 ms

# testing if ab/cd=a/c or b/d as told us
def cancelling_fractions(numerator,denominator):
    n_1=numerator//10
    n_2=numerator%10
    d_1=denominator//10
    d_2=denominator%10
    temp_div=numerator/denominator

    return (n_1==d_2 and n_2/d_1==temp_div) or (n_2==d_1 and n_1/d_2==temp_div)

numerator=1
denominator=1
for i in range(10,100):
    for j in range(10,i):
        if i%10!=0 and j%10!=0  and cancelling_fractions(j,i): # avoid division by 0
            numerator*=j
            denominator*=i

# minimal fraction, dividing all common divisors
for i in range(2, numerator + 1):
    while numerator%i==0 and denominator%i==0:
        numerator//=i
        denominator//=i

print(numerator, denominator)
#Answer: 100
