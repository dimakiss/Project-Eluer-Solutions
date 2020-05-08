
# Solution to problem 48
# https://projecteuler.net/problem=48
# Run time  221.17 ms

sum=0

for i in range(1,1000):
    tempmult=1
    for j in range(i):
        tempmult*=i
        tempmult%=10**10
    sum+=tempmult
    sum%=10**10

print(sum)
# Answer: 9110846700
