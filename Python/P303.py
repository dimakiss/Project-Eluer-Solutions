
# Solution to problem 303
# https://projecteuler.net/problem=303
# Run time 174396 ms

def toStr(n,base=3):
    
    # convert to base 3
    
    convertString = "012"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]
lst=[1]
def test(num):

    for i in lst:
        if i%num==0:
            return i
    return 0

def test2(num):

    # expending the lst for the exceptions

    temp = int(str(lst[-1]),3)
    t=int(toStr(temp))
    while t % num != 0:
        lst.append(t)
        temp += 1
        t = int(toStr(temp))
    return int(toStr(temp))
sum=0
tester=[]

# the max number which in base 3 is divisable by 1<i<10000 except some excaptions is 2420280
# so lst is all numbers till 2420280 in base 3
for i in range(1,2420280):#1764915561
    lst.append(int(toStr(i)))

# finds the number in base 3 which divisible by i 
for i in range(1,10001):
    t=test(i)
    sum+=t//i
    if t==0: # exceptions
        tester.append(i)
        #print(i)
        
last=test(99)
lst=[lst[-1]] # all exceptions are not divisble by all the numbers in lst
for i in tester:
    if i==999 or i==9999: # 99-> 1122222222 ; 999->111222222222222 9999-> 11112222222222222222
                          # rear exception found menually
        while last % i!=0:
            last = int("1"+str(last)+"2222")
        t=last
    else:
        temp=test(i)
        if temp==0:
            t=test2(i)
        else:
            t=temp

    lst.append(t)
    sum+=t//i
print(sum)
#Answer: 1111981904675169
