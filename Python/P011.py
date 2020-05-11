
# Solution to problem 11
# https://projecteuler.net/problem=11
# Run time  1.62ms

#prodact of 4 numbers in a row
def side(numbers):
    maxmult=0
    for row in numbers:
        for i in range(len(row) - 4):
            maxmult = max(maxmult, row[i] * row[i + 1] * row[i + 2] * row[i + 3])
    return maxmult

#prodact of 4 numbers in a column
def up(numbers):
    maxmult=0
    for i in range(len(numbers)):
        for j in range(len(numbers)-4):
            maxmult = max(maxmult, numbers[i][j]*numbers[i][j+1]*numbers[i][j+2]*numbers[i][j+3])
    return maxmult

#prodact of 4 numbers in a down diagonal
def diagdown(numbers):
    maxmult=0
    for i in range(len(numbers)-4):
        for j in range(len(numbers)-4):
            maxmult = max(maxmult, numbers[i][j]*numbers[i+1][j+1]*numbers[i+2][j+2]*numbers[i+3][j+3])
    return maxmult

#prodact of 4 numbers in an up diagonal
def diagup(numbers):
    maxmult=0
    for i in range(len(numbers)-4):
        for j in range(len(numbers)-4):
            maxmult = max(maxmult, numbers[i+3][j]*numbers[i+2][j+1]*numbers[i+1][j+2]*numbers[i][j+3])
    return maxmult

#read number with numbers.txt
f = open("numbers.txt", "r")
numbers_str=f.read()
numbers=[]
for i in numbers_str.split("\n"):
    row=[]
    for j in i.split(' '):
        row.append(int(j))
    numbers.append(row)


print(max(side(numbers),up(numbers),diagdown(numbers),diagup(numbers)))
# Answer: 70600674
