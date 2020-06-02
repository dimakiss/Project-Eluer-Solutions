
#Solution to problem 93
#https://projecteuler.net/problem=93
#Run time 2946 ms


t=1
mod=10000000000
for i in range(7830457):
   t=(t*2)%mod
t*=28433
t+=1
t%=mod
print(t)
#Answer: 8739992577
