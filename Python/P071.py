
#Solution to problem 71
#https://projecteuler.net/problem=71
#Run time 2035 ms

max=3/7
min=0
ti=0
tj=0
for i in range(1,1000001):
    for j in range(int(min*i),i):
        if j/i>max:
            break
        elif j/i<max and j/i>min:
            min=j/i
            #print(min)
            ti=i
            tj=j
#devide by the greatest common factor

for i in range(2,int(math.sqrt(ti)+1)):
    while ti%i==0 and tj%i==0:
        ti//=i
        tj//=i
print(tj,ti)
#Answer: 428570
