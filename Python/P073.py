
#Solution to problem 73
#https://projecteuler.net/problem=73
#Run time 12022 ms



d={}
max=1/2
min=1/3
for i in range(1,12001):
    for j in range(int(min*i),i): # Example min =2/5 next we check for 1/6 2/6.. not need to check 1/6 we will start from 
                                  # (2/5)*6 which is 2 so 2/6 will be the starter  
        if j/i>max:
            break
        elif j/i<max and j/i>min:
            d[j/i]=1
print(d.__len__())
#Answer: 428570
