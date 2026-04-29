# Q1: Take a string and count frequency of each character using dictionary

s = input("Enter string: ")
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d);


#2: Take a list of numbers and count frequency of each number using dictionary.
nums = list(map(int, input("Enter your number : ").split()))
d = {}
for i in nums:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)

        