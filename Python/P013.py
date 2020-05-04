
# Solution to problem 13
# https://projecteuler.net/problem=13
# Run time  0.85 ms

# numbers.txt is the 100 numbers
f = open("numbers.txt", "r")
numbers=(f.read()).split('\n')
tempsum=0

#Took every number out of the 100 and summed the last 10 digs and update the original number my trimming it
#and the summed partial number devived by 1000000000
for i in range(5):
    for j in range(numbers.__len__()):
        tempsum+=int(numbers[j][-10:])
        numbers[j]=numbers[j][0:-10]

    if i!=4:
        tempsum //= 10 ** 10


print(str(tempsum)[0:10])
# Answer: 5537376230
