# Q1: Take a string and count frequency of each character using dictionary

s = input("Enter string: ")
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d);

