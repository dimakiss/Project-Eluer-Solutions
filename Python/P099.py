
#Solution to problem 99
#https://projecteuler.net/problem=99
#Run time 2 ms


# the numbers
with open("text.txt",'r') as f:
    buff=f.read()
max_num=0
max_i=0

# if n1^n2 =t --> n2*log(n1)=log(t) and we will look for the gradest log(t)
for i in buff.split('\n'):
    temp_str=i.split(',')
    temp_str=int(temp_str[1])*math.log10(int(temp_str[0]))
    if max_num<temp_str:
        max_num=temp_str
        max_i=buff.split('\n').index(i)
print(max_i+1) # starts from 0
#Answer: 709
