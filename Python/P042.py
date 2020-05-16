
# Solution to problem 42 
# https://projecteuler.net/problem=42
# Run time less then 0ms

#caclate the value of every word
def value(word):
    count=0
    for i in word:
        count+=ord(i)-ord('A')+1
    return count

# we have to solve N^2+N-2TN if N is a whole number so TN is triangle numbers when TN is the current word value
def is_tring_word(word):
    word_value=value(word)
    return int((1+8*word_value)**0.5)==((1+8*word_value)**0.5) # square of (b^2 -4ac) --> square(1+8Tn)
                                                               # if this number (N) is float there is no Nth term
                                                               # which equal TN (value of word)
# saves all words 
f = open("words.txt", "r")
words=f.read().split(',')
f.close()

count_tring_words=0
for word in words:
    word=word.split('"')[1]
    if is_tring_word(word):
        count_tring_words+=1

print(count_tring_words)
# Answer: 162
