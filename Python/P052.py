
# Solution to problem 52
# https://projecteuler.net/problem=52
# Run time 785.03ms

# compere the digits of num1 and num2
def is_in(num1,num2):
    lst=[0]*10
    while num1!=0 or num2!=0:
        lst[num1%10]+=1
        lst[num2%10]-=1
        num1//=10
        num2//=10
    for i in range(lst.__len__()):
        if lst[i]!=0:
            return False
    return True


found=False
num=0

while found==False:
    num+=1
    found = True
    for i in range(2,7):
        if is_in(num,num*i):
            pass
        else:
            found = False
            break

print(num)
#Answer: 142857
