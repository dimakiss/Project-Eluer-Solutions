
# Solution to problem 43
# https://projecteuler.net/problem=43
# Run time 12954 ms


# generate all possible numbers length 'len' form the list 'lst'
def get_numers(len,lst,number=None,d=None):
    if number is None:
        return get_numers(len,lst,"",{})
    if len==1:
        for i in lst:
            temp=number+i
            
            # check
            if int(temp[7:10]) % 17 == 0 and int(temp[6:9])%13==0 and int(temp[5:8])%11==0 and  int(temp[4:7])%7==0 and\
                    int((temp)[5])%5==0  and int(temp[2:5])%3==0  and  int((temp)[3])%2==0 :
                d[int(temp)]=d.__len__()
    for i in lst:
        temp_lst=lst.copy()
        temp_lst.remove(i)
        get_numers(len-1,temp_lst,number+i,d)
    return d

lst=["0","1","2","3","4","5","6","7","8","9"]
max_prime=0
sum_pan=0
a=get_numers(10,lst)
for i in a:
    sum_pan+=i
print(sum_pan)

#Answer: 16695334890
