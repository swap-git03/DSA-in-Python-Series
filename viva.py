# To check palindrome
word = input("Enter word")
rev = word[::-1]

if rev == word:
    print('is palindrome')
else :
    print('no pali')

# 1️⃣ Reverse a String (without slicing)
 
word = input('ENter your string')
rev = ""
 
for i in word:
     rev = i + rev
print(rev)
     