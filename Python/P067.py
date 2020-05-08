##### same code as for problem 18
#---------------------------------
# Solution to problem 67
# https://projecteuler.net/problem=67
# Run time  9.92 ms

# numers.txt is the list of number
f = open("xor.txt", "r")
numbers = (f.read()).split('\n')  # slpiting the lines
lst = []
# splitting the numbers in every line and converting to int
for i in numbers:
    temp = []
    for j in i.split(' '):
        temp.append(int(j))
    lst.append(temp)

#   2    --> #      2        #    2      #   2    # 2+15
#  3 5       #    3   5      #  3   5    # 13 15
# 1 2 3      # 1+9 2+8 3+7   # 10 10 10
# 9 8 7 6     #9   8   7   6

# by starting for the end and calculation the maximum path and ignoring the non-maximum path
for i in range(lst.__len__() - 2, -1, -1):
    for j in range(lst[i].__len__()):
        lst[i][j] += max(lst[i + 1][j], lst[i + 1][j + 1])
print(lst[0])
# Answer: 7273
