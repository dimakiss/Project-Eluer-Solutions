
# Solution to problem 8
# https://projecteuler.net/problem=8
# Run time  1.87ms

#This solution is to take the initial 13 dig number and add the next number and erase the last number
#It's more efficient then multiplying every time 13 digs

#read file with numbers
f = open("numbers.txt", "r")
numbers=f.read()
temp_num=1

zf=0 #kind of a register if there 0 in the sequence if it's don't calculate the product because is supposed to be 0
for i in range(13):
    if int(numbers[i])==0 :
        zf+=1
    else:
        temp_num *= int(numbers[i])
print(zf)
max_prod=0

for i in range(0,numbers.__len__()-13):
    if zf == 0:
        max_prod = max(max_prod, temp_num)
    if numbers[i + 13] == "0":
        zf += 1
    else:
        temp_num *= int(numbers[i + 13])
    if numbers[i] == "0":
        zf -= 1
    else:
        temp_num //= int(numbers[i])
print(max_prod)
# Answer: 23514624000
