
# Solution to problem 45
# https://projecteuler.net/problem=45
# Run time 49.77 ms


# by using x1,2=-b(+-)sqrt(b^2-4ac)/2 the quadratic equation we can look at every equation and find if current number
# is product of this equation (if its whole value)

def is_Triangle(num):
    determinant=1+4*2*num
    return int(determinant**0.5)==determinant**0.5 and int(determinant**0.5)%2==1

def is_Pentagonal(num):
    determinant=1+(4*2*3*num)
    return int(determinant**0.5)==determinant**0.5 and int(determinant**0.5)%6==5

def culc_Hexagonal(n): # calc hex number by n
    return n*((2*n)-1)
n=144
num=culc_Hexagonal(n)
while not is_Pentagonal(num) or not is_Triangle(num):
    n+=1
    num = culc_Hexagonal(n)
print(num)
# Answer: 1533776805
