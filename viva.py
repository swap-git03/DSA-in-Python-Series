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
     

# dont push below 
# check prime 
num = int(input("Enter number: "))
flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1
        break

if flag == 0 and num > 1:
    print("Prime")
else:
    print("Not Prime")

# armstrong
num = int(input("Enter number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit * digit * digit
    num = num // 10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")

# print numbers from 1-n
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# mult tabke 
# num = int(input("Enter number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1

# even numbers from 1-n
# even off
num = int(input('enter num'))
i = 1
while ( i<=num ):
    if i % 2 == 0:
        print(f"even numbers are {i}")
    i = i + 1
    