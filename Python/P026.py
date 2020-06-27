
# Solution to problem 26
# https://projecteuler.net/problem=26
# Run time 5426 ms

# calculate the repeating decimal of 1/d
# if it's not repeating returns 0
def div(num,l):
    s=""
    temp=1
    flag=False
    while s.__len__()<10+l:
        if temp==0:
            return '0'
        elif temp<num:
            temp*=10
            if flag:
                s+='0'
            flag=True
        else:
            flag=False
            s+=str(temp//num)
            temp%=num
    return s[:l]

#finds the repeating pattern in some sample
def pattern(samp):
    for start in range(10):
        for le in range(1, samp.__len__() // 6):
            found=True
            for i in range(le):
                if samp[i+start]!=samp[le + i + start] or samp[i + start]!=samp[2 * le + i + start]:
                    found = False
                    break
            if found:
                return samp[start:le + start]

max_len=0
number=0
for i in range(11,1000):
    samp=div(i,6*i)
    if samp=='0':
        continue
    patt=pattern(samp)
    if patt.__len__()>max_len:
        number=i
        max_len=patt.__len__()
        
print(number)
#Answer: 983
