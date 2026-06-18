# ◆ Beginner
# 41. Reverse a string.
name = "abcdef"
rev_name = name[::-1]
print(rev_name)

# 42. Check if a string is a palindrome.
name1 = input("Enter first name : ")
name2 = input("Enter second name : ")
sec_name = name2[::-1]
if name1 == sec_name:
    print('Is Palindrome')
else:
    print('Not a palindrome')


# 43. Count the number of vowels in a string.
word = input("Enter word : ")
vow = ['a','e','i','o','u']
count_vow = 0
for ch in word:
    if ch in vow:
        count_vow += 1
print(count_vow)

# 44. Convert a sentence to uppercase, lowercase, and title case.
sentence =  input("Enter sentence : ")
print(sentence.upper())
print(sentence.lower())
print(sentence.title())

# 45. Count the total number of words in a sentence
sentence =  input("Enter sentence : ")
words = sentence.split()
print(len(words))



# ◆ Intermediate
# 46. Count the frequency of each character in a string.
stri = input("Enter string : ")
d = {}
for i in stri:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
# 47. Remove a