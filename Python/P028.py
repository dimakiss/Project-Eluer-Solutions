
# Solution to problem 28
# https://projecteuler.net/problem=28
# Run time  0.37 ms

num=1
# by some math we can see that the right diagonal is the square of odd number the spiral in subtraction
# i-1 whenever i is the number for example with 25 i=5 the first number is 25 -4=21 21-4=17
#17-4=13 

for i in range(3,1002,2):
    root=i*i
    num+=4*root-(1+2+3)*(i-1)
print(num)
# Answer: 669171001
