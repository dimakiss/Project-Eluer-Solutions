
# Solution to problem 31
# https://projecteuler.net/problem=31
# Run time 3240 ms

lst=[200,100,50,20,10,5,2,1]
def different_ways(num, m_max=0):

    # takes every number and subtract the con value until its equal to 0
    # it will run through all the possible options
    # m_max stands for non repeating arranges EX: 5--> 2,1,1,1 and 1,1,1,2
    # every number the comes after each number is grader or equal to the current number 2=>2=>1 =5


    sum=0
    if num==0:
        return 1
    for i in lst:
        if num>=i and m_max<=i:
            sum+=different_ways(num - i, i)

    # Can use this instead:
    # Run time 2347 ms

    # if num >= 200 and m_max <=200:
    #     sum += different_ways(num - 200, 200)
    # if num >= 100 and m_max <=100:
    #     sum += different_ways(num - 100, 100)
    # if num >= 50 and m_max <=50:
    #     sum += different_ways(num - 50, 50)
    # if num >= 20 and m_max <=20:
    #     sum += different_ways(num - 20, 20)
    # if num >= 10 and m_max <=10:
    #     sum += different_ways(num - 10, 10)
    # if num >= 5 and m_max <=5:
    #     sum += different_ways(num - 5, 5)
    # if num >= 2 and m_max <=2:
    #     sum += different_ways(num - 2, 2)
    # if num>=1 and m_max <=1:
    #     sum+=different_ways(num - 1, 1)
    return sum

print(different_ways(200))
#Answer: 73682
