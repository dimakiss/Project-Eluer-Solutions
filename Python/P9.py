
# Solution to problem 9
# https://projecteuler.net/problem=9
# Run time  152.81ms

#a^2+b^2=c^2
#c=1000-a-b --> a+b<500 <-- a<b<c

for a in range(1,500):
    for b in range(a,500):
        c=(a**2+b**2)**0.5
        if c%1==0.0 and int(a+b+c)==1000:
            print(a*b*c)

# Answer: 1152.81
