
# Solution to problem 39
# https://projecteuler.net/problem=39
# Run time  27054.02 ms

p=[0]*1000
for a in range(350):
    for b in range(a,400):
        for c in range(b,1000-(a+b)):
            if c == (a ** 2 + b ** 2) ** 0.5 :
                p[a+b+c]+=1
max=0
for i in range(p.__len__()):
    if p[max]<p[i]:
        max=i
print(max)
# Answer: 840
