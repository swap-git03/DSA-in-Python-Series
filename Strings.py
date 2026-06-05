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
word = input("Enter word : ")
d = {}
for i in word:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)

# 47. Remove all spaces from a string.
word = input("Enter word : ")
print(word.replace(" ", ""))

# 48. Replace all vowels in a string with *.
word = (input('Enter word : '))
new_word = ""
vow = ['a','e','i','o','u']
for i in word:
    if i in vow:
        new_word += "*"
    else:
        new_word += i 
print(new_word)

# 49. Check if two strings are anagrams of each other.
word1 = list(input('Enter first word : '))
word2 = list(input('Enter second word : '))
word1.sort()
word2.sort()
if word1==word2:
    print('is anagram')
else:
    print('not a anagram')

# 50. Find the longest word in a sentence.
sentence = (input('Enter a full sentence : '))
words = list(sentence.split())
longest = ""
for i in words:
    if len(i) > len(longest):
        longest = i
print(longest)
    

# 51. Reverse each word in a sentence (e.g., 'hello world' → 'olleh dlrow').
sentence = (input('Enter a full sentence : '))
words = sentence.split()
result = ""
for i in words:
    rev = ""
    for j in range(len(i)-1, -1, -1):
        rev += i[j]
    result += rev + " "

print(result)


# 52. Check if a string contains only digits, only alphabets, or is mixed.
word = (input('Enter a full sentence : '))
alphabet_flag = False
digit_flag = False
special_flag = False
for i in word:
    if i.isalpha():
        alphabet_flag = True
    elif i.isdigit():
        digit_flag = True
    else:
        special_flag = True
print(alphabet_flag,digit_flag,special_flag)


# 53. Remove duplicate characters from a string while preserving order.
word = (input('Enter a full sentence : '))
new_word = ''
for i in word:
    if i not in new_word:
        new_word += i
print(new_word)