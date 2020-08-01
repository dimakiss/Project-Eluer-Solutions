
# Solution to problem 62
# https://projecteuler.net/problem=62
# Run time 763 ms


def to_ordered(num):

# split numbers

    temp=[]
    for i in str(num):
        temp.append(i)

    temp.sort()
    temp.reverse()
    temp="".join(temp)
    return temp

list_s=[]   #   list of all sorted cubes
list_cube_count=[]  #   list counter of cubes
list_smallest_reminder=[] # list holder for smallest cube permutation
i=2

while True:
    i+=1
    temp=i**3
    temp_sort=to_ordered(temp)
    if temp_sort in list_s:
        list_cube_count[list_s.index(temp_sort)]+=1
        if list_cube_count[list_s.index(temp_sort)]==5:
            print(list_smallest_reminder[list_s.index(temp_sort)])
            break
    else:
        list_cube_count.append(1)
        list_s.append(temp_sort)
        list_smallest_reminder.append(temp)


# Answer: 127035954683
