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

# 47. Remove all spaces from a string.
str1 = input("Enter string : ")
str2 = ""
for i in str1:
    if i != " ":
        str2 += i 
print(str2)

# 48. Replace all vowels in a string with *.
str1 = input("Enter string : ")
vow = ['a','e','i','o','u']
str2 = ""
for i in str1:
    if i in vow:
        str2 += "*"
    else:
        str2 += i
print(str2)


# 49. Check if two strings are anagrams of each other.
str1 = input("Enter String 1 : ")
str2 = input("Enter String 2 : ")
d1 = {}
d2 = {}
for i in str1:
    if i in d1:
        d1[i] +=1
    else:
        d1[i] = 1
for i in str2:
    if i in d2:
        d2[i] +=1
    else:
        d2[i] = 1
if d1 == d2:
    print('Are Anagram')
else:
    print('Not an anagram')


# 50. Check whether a substring is present in a string.
text = input("Enter main string : ")
substring = input("Enter substring to search : ")
if substring in text:
    print("Substring found")
else:
    print("Substring not found")
