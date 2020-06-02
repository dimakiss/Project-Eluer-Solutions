
#Solution to problem 100
#https://projecteuler.net/problem=100
#Run time 6 ms

number=1000000000000
n = 21 # number
b=15 # blue
# n*(n-1)=2*b*(b-1) --> n^2-n-2b^2-2b
# Recursive solution to 2 variable equation
# https://www.alpertron.com.ar/QUAD.HTM#:~:text=This%20calculator%20can%20solve%20equations,and%20y%20are%20integer%20numbers.
while (n < number):
    blue_t = 3 * b + 2 * n - 2
    n_t = 4 * b + 3 * n - 3

    b = blue_t
    n = n_t

print(b)
#Answer: 756872327473
