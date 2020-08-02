
# Solution to problem 24
# https://projecteuler.net/problem=24
# Run time 0 ms

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


s = "0123456789"
num = 10 ** 6 + 1
new_s = ""
for i in range(9, 0, -1):
    fact = factorial(i)
    index = num // fact
    num %= fact
    new_s += s[index]
    s = s[:index] + s[1 + index:]

new_s += s
print(new_s)

# Answer: 2783915460
