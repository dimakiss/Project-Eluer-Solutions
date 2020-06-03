#Solution to problem 104
#https://projecteuler.net/problem=104
#Run time 61041 ms

def te(num):
    num=str(num)[-9:]
    d={}
    d['0']=1
    for char in num:
        d[char]=1
    del d['0']
    return d.__len__()==9
decimal.getcontext().prec=20
pai=(decimal.Decimal.sqrt(decimal.Decimal(5))+decimal.Decimal(1))/decimal.Decimal(2)
num=2
temp1=1
counter=3
mod=1000000000

while True:
    if te(int(num)):
        tera=int(pai**counter)/decimal.Decimal(math.sqrt(5))
        tera = str(tera).replace('.', '')
        print(counter)
        if te(str(tera)[:9]):
            break
    counter+=1
    #calc fib number
    num=num+temp1
    temp1=num-temp1
    num%=mod
    temp1%=mod

print(num,counter)
#Answer: 329468
