
# Solution to problem 5
# https://projecteuler.net/problem=5
# Run time 0.13ms

# prime_factor get n as number
# prime_factor return the list of the primes factor and their power for expample 42=2^1 * 3^1 * 7^1 ---> [[2,1],[3,1],[7,1]]
def prime_factor(n):
    lst=[]
    for i in range(2,int(n**0.5)+1):
        counter=0
        while n%i==0:
            counter+=1
            n//=i
        if counter!=0:
            lst.append([i,counter])
            counter=0
    if n>1:
        lst.append([n, 1])
    return lst

# smallest_multiple get n as the number
# smallest_multiple returns the minimal number that divisible by all number from 1-n
def smallest_multiple(n):
    lst=[[0,0]]*(n+1)
    num=1
    for i in range(2,n+1):
        lst_temp=prime_factor(i)
        # This loop build the minimal list (which represent prime factors of some number) and the difference between the
        # current loop and the updated one will be added as multiplication to the number,
        # by that it saves me an extra loop to calculate back a number from the list of his factors and their power
        for j in lst_temp:
            num*=j[0]**max(0,j[1]-lst[j[0]][1]) # if the difference is negative the current power is already maximal
            lst[j[0]]=[j[0],max(lst[j[0]][1],j[1])] # update

    return num

print(smallest_multiple(20))
# Answer: 232792560
