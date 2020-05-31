# Solution to problem 17
# https://projecteuler.net/problem=17
# Run time 1.06 ms


names=["","one","two","three", "four","five","six","seven","eight","nine","ten",
       "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
tens=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

lst=[0]
counter=11 # "one thousand"
for i in range(1,1000):
    number=0

    if i <=20: # fill the names list
        number=names[i].__len__()
    elif i<100: # if we need to add the "hundred"
        number = tens[i//10].__len__() + lst[i % 10]
    elif i%100==0: # if we need to add the "hundred and" or just "hundred" if number%100 ==0 no need for the "and"
                   # 200 "two hundred"
        number = lst[i // 100]+7
    else: # if larger then 100 and not divisable by 100 "hundred and" something.. (342 ("three hundred and forty-two"))
        number=lst[i//100]+10+lst[i%100]
    lst.append(number)
    counter+=number

print(counter)
# Answer: 21124
