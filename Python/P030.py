
# Solution to problem 30
# https://projecteuler.net/problem=30
# Run time  1381.76 ms

sum=0
# we can predict that the highest number is 325836 --> maximu diget is 9 so 9^5*n where n is the numbers length
# so 9^5 *n should always be grater then 10^n or even equal to is for our problen
# so when 10^n is alway equal we have a problen
# when 9^5 *n -10^n <0 its to upper limit or n=5.513 so the upper limit is 10^5.513 or 325836.701->325836
for i in range(2,325836):
    temp=i
    temp_sum=0
    while temp>0:
        temp_sum+=(temp%10)**5
        temp//=10
    if temp_sum==i:
        sum+=temp_sum
        print(i)
print(sum)
# Answer: 443839
