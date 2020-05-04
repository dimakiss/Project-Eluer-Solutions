
# Solution to problem 20
# https://projecteuler.net/problem=20
# Run time  31.63 ms



lst=[0]*280 # the number is atleast 2 dig long for 99-10=89*3=267 +3(the last 100) + the first 1-10 diges
             # i gave an extra 10
lst[-1]=1
print(lst)
num=1
mult=2
# by braking the large number into diges that multing every dig by bult
# which getting bigger
for i in range(2,100):
    temp=0
    num=0
    for j in range(lst.__len__()-1,-1,-1):
        lst[j]=lst[j]*mult+temp%10
        temp//=10 # temp the extra of the dig can be bigger tehn 10 9*80 for example
        temp+=lst[j]//10
        lst[j]%=10
        num+=lst[j]
    mult += 1
print(num)
# Answer: 648
