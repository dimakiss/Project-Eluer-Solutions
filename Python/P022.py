
# Solution to problem 22
# https://projecteuler.net/problem=22
# Run time  17.88 ms

# calculate every char relative to 'A'
def calc_name(str):
    value=0
    for i in str:
        value+=ord(i)-ord("A")+1
    return value
# all the names are in names.txt
f = open("names.txt", "r")
names=(f.read()).replace('"','').split(',')

names.sort() # used python default list sort
sum=0 #counter
for i in range(0,names.__len__()):
    sum+=(i+1)*calc_name(names[i])
print(sum)
# Answer: 871198282
