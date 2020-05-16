
# Solution to problem 63
# https://projecteuler.net/problem=63
# Run time 2.97ms

count =0
for i in range(1,10): #i^j if i is greater  then 10 i^j will always larger then j len
    for j in range(1,100):
        if str(i**j).__len__()==j:
            print(i**j ,"  ", i,"^",j)
            count+=1

print(count)
# Answer: 49
