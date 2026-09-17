# Check whether it is positive, negative, or zero.
# If positive, print whether it is even or odd.
# Calculate the sum of numbers from 1 to n.
# Count how many numbers between 1 and n are divisible by 3.
# Print all results clearly.

n = int(input("Enter a number : "))
if n > 0:
  print(f'{n} is Positive')
  if n % 2 == 0:
    print('NUMBER IS EVEN')
  else:
    print('NUMBER IS ODD')
else:
  print('f{n} is -ve')

sum = 0
for i in range(1, n+1):
  sum += i
print(f'sum is {sum}')

count = 0
for j in range(1, n+1):
  if j % 3 == 0:
    count += 1
print(f'number divisible by 3 bet 1 to n is {count}')


# Take a string from the user and:

# Print the string in reverse.
# Count the number of vowels.
# Count the number of consonants.
# Count how many times a particular character occurs.
# Print whether the string is a palindrome.
word = input("Enter a string : ")
rev_word = ""
for i in word:
  rev_word = i + rev_word
print(f'{word} is your input')
print(f'{rev_word} is thereversed word')

vow = 'a','e','i','o','u'
vowels = 0
consonents = 0
for j in word:
  if j in vow:
    vowels += 1
  else:
    consonents += 1
print(f'{vowels} are total vowels')
print(f'{consonents} are total consonents')

a_in_word = 0
for k in word:
  if k == 'a':
    a_in_word+=1
print(f'A in word {a_in_word}')

if word == rev_word:
  print('Palindrom')
else:
  print('Not a palindrom')



# Print the list.
# Calculate the sum without sum().
# Count how many numbers are even.
# Find the largest number without max().
# Find the smallest number without min().
# Create a new list containing only numbers greater than 10.
# Create a new list containing the squares of even numbers.
num = [12, 5, 8, 21, 10, 7, 30, 4]
total = 0
for i in num:
  total += i
print(f'{total} is sum')

even_nums = 0
for j in num:
  if j%2==0:
    even_nums += 1
print(f'total even nums are {even_nums}')

largest = 0
for k in num:
  if k > largest:
    largest = k
print(f'Largest numner is {largest}')


smallest = num[0]
for k in num:
  if k < smallest:
    smallest = k
print(f'smallest numner is {smallest}')

great10 = []
for l in num:
  if l > 10:
    great10.append(l)
print(f'Numbers greater than 10 are{great10}')

squaredlist = []
for m in num:
  if m%2==0:
    m = m * m
    squaredlist.append(m)
print(f'Square of numbers are {squaredlist}')