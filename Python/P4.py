# Solution to problem 4
# https://projecteuler.net/problem=4
# Run time 5ms

# is_palindrome get n as number
# is_palindrome return if the number is polindrom
def is_palindrome(num):
    str_num=str(num)
    while str_num.__len__()>=2:
        if str_num[0]!=str_num[-1]:
            return False
        str_num=str_num[1:-1]
    return True

# largest_palindrome_product get null
# largest_palindrome_product return largest palindrome made from the product of two 3-digit numbers
def largest_palindrome_product():
    product=0
    max=0
    for i in range(999,900,-1):
        for j in range(i,900,-1):
            if is_palindrome(i*j) and max<i*j:
                max=i*j
                i=900
    return max

print(largest_palindrome_product())
# Answer: 906609
