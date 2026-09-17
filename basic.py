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