
# Solution to problem 36
# https://projecteuler.net/problem=36
# Run time  975.45 ms

# is_palindrome get n as number
# is_palindrome return if the number is polindrom
def is_palindrome(num):
    str_num=str(num)
    while str_num.__len__()>=2:
        if str_num[0]!=str_num[-1]:
            return False
        str_num=str_num[1:-1]
    return True
sum=0
for i in range(1000000):
    if is_palindrome(i):
        if is_palindrome(bin(i)[2:]):
            sum+=i
print(sum)
# Answer: 872187
