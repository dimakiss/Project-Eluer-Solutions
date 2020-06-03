
#Solution to problem 32
#https://projecteuler.net/problem=32
#Run time 3786 ms

# generate numbers from list by len
#, for example, we want all numbers len 3 out of the list [1,2,3,4] we have 4 option for first
# 3 for a second so on so 4*3*2

# the only options for a*b=c when a,b,c pandigital 1-9 are when a=1 and b=4 so c is 5 dig len or
# a=2 b=3 c=5 len(a)+len(b)=len(c) and len(a)+len(b)+len(c)=9

def get_numers(len,lst,number=None,d=None):
    if number is None:
        return get_numers(len,lst,"",{})
    if len==1:
        for i in lst:
            d[(number+i)]=1
    for i in lst:
        temp_lst=lst.copy()
        temp_lst.remove(i)
        get_numers(len-1,temp_lst,number+i,d)
    return d

d1={} # collector for all the products
# check if pandigital (a+b+c as string)
def pandigital(num):
    lst=[]
    for i in num:
        if i not in lst:
            lst.append(i)
        else:
            return False
    return lst.__len__()==9 and "0" not in lst #len 9 and only 1-9

# gets number and list of 1-9, by removing from the list the numbers that appear in number we can produce numbers more efficient
def check(number,lst):
    counter=0
    _len=5-len(number)
    lst_copy=lst.copy()
    for i in number:
        lst_copy.remove(i)
    b=get_numers(_len,lst_copy,"",{})
    for i in b:
        prod=int(number)*int(i)
        if pandigital(str(prod)+i+number):
            d1[prod]=1




lst=["1","2","3","4","5","6","7","8","9"]
a=get_numers(3,lst)
a.update(get_numers(4,lst))
counter=0
for i in a:
    check(i,lst)

for i in d1:
    counter+=i

print(counter)
#Answer: 45228
