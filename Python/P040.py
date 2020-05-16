
# Solution to problem 40
# https://projecteuler.net/problem=40
# Run time 0.43ms

str_num=""
len=1
i=1
product=1

#while len smaller then 1000000
while len<1000000:
    i+=1
    str_num=str(i)
    len+=str_num.__len__() #len of number "1095".len=4
    log10=math.log10(len) 
    if int(log10)!=int(math.log10(len-str_num.__len__())): ## check if we switch from 99.. to 100.. (99 to 100+) 
        number=10**round(log10)-len 
        print(i,number,str_num[number-1]) # trind every number that comatin our d10..0
        product*=int(str_num[number-1])
print(product)
# Answer: 210
