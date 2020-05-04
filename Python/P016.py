
# Solution to problem 16
# https://projecteuler.net/problem=16
# Run time  285.98 ms

lst=[0]*333 #2^n is no longer then n/2 because 2^n=8^n/3 which samller then 10^n/3 which is 10^333 means length=333 
            # at most
lst[-1]=1
print(lst)
num=0
#created list, the last number at the start is 1 and whole list multiplied by 2
for i in range(1000):
    temp=0
    num=0
    for j in range(lst.__len__()-1,-1,-1):
        lst[j]=lst[j]*2+temp
        temp=lst[j]//10 #making sure every place j in the list represent the j-th number in the multiple of 2^i
        lst[j]%=10
        num+=lst[j]
print(num)
# Answer: 1366
