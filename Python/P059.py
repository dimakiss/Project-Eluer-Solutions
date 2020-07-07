# Solution to problem 59
# https://projecteuler.net/problem=59
# Run time 54 ms

with open("p059_cipher.txt",'r') as f:
    buffer=f.read().split(',')


chars=[] # all characters a-z
normal=['.',',',"'",'!','?','"'," ",')','(',' ',':',';','-','}','{','[',']','+','/'] # normal characters
for i in range(ord('a'),ord('z')+1):
    chars.append(chr(i))

sum=0
for a in chars:
    for b in chars:
        for c in chars:
            found=True
            lst=[a,b,c]
            for i,char in enumerate(buffer):
                asci=int(char)^ord(lst[i%3])
                new=str(chr(asci))
                sum+=asci
                if not str.isalpha(new) and new not in normal and not str.isnumeric(new):
                    sum=0
                    found=False
                    break
            if found:
                chars=[] # brake all 3 loops
                print(sum)
#Answer: 129448
