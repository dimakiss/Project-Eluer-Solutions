
# Solution to problem 41
# https://projecteuler.net/problem=41
# Run time 2913 ms

#is_prime get n as the number
#is_prime return True or False if the number is a prime number
def is_prime(n):
    if n%2==0 and n!=2 or n==1:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

# generate all possible numbers length 'len' form the list 'lst'
def get_numers(len,lst,number=None,d=None):
    if number is None:
        return get_numers(len,lst,"",{})
    if len==1:
        for i in lst:
            d[(number+i)]=d.__len__()
    for i in lst:
        temp_lst=lst.copy()
        temp_lst.remove(i)
        get_numers(len-1,temp_lst,number+i,d)
    return d

lst=["1","2","3","4","5","6","7","8","9"]

max_prime=0
for k in range(9,-1,-1):
    a = get_numers(k, lst[:k])
    for i in a:
        if is_prime(int(i)):
            max_prime=max(max_prime,int(i))
    if max_prime!=0:
        break

print(max_prime)
#Answer: 7652413
