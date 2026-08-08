num = [10, 15, 20, 25, 30, 35, 40]

# Q1  Print every element using a for loop.
for i in num:
    print(i, end=" ")
print()
print()

# Q2  Print only the even numbers.
for i in num:
    if i%2==0:
        print(i, end=" ")
print()
print()

# Q3  Print only the numbers greater than 20.
for i in num:
    if i > 20:
        print(i, end=" ")
print()
print()

# Q4  Count how many numbers are divisible by 5.
count=0
for i in num:
    if i%5==0:
        count += 1
print(count)
print()

# Q5  Create a variable total and calculate the sum of all elements.
total=0
for i in num:
    total=total+i
print(total)
print()

# Q6   Modify the existing list so every number becomes double.
for i in range(len(num)):
    num[i]=num[i]*2
print(num)
print()


# Q7 Modify the list so every even number becomes its square.
# Odd numbers should remain unchanged.
num = [10, 15, 20, 25, 30, 35, 40]

for i in range(len(num)):
    if num[i]%2==0:
        num[i]= num[i]*num[i]
print(num)
print()

# Q8 Find the maximum value in the list without using max().
num = [10, 15, 20, 25, 30, 35, 40]
maxi=0
for i in num:
    if maxi<i:
        maxi = i
print(maxi)
print()

# Q9 Find the minimum value without using min().
num = [10, 15, 20, 25, 30, 35, 40]
mini=num[0]
for i in num:
    if i<mini:
        mini = i
print(mini)
print()
# Q10 Count how many numbers are:
# even & odd
# Print both counts
num = [10, 15, 20, 25, 30, 35, 40]
even=0
odd=0
for i in num:
    if i % 2 ==0:
        even +=1
    else:
        odd +=1
print(f"even nums are {even}")
print(f"odd nums are {odd}")

num = [40, 10, 30, 20, 30, 50, 20,30]
# Q1Find how many times 20 occurs.
x = num.count(20)
print(x)
# Q2Find the first index of 30.
a=num.index(30)
print(a)

# Q3Sort the list ascending.
num.sort()
print(num)
# Q4Now sort it descending.
num.sort(reverse=True)
print(num)
# Q5Reverse this list:
a = [10, 50, 20, 40, 30]
a.reverse()
print(a)
print(60 in num)
# Q7Create a copy of num called backup.
backup=num.copy()
print(backup)
# Q8Clear backup and print both backup and num.
backup.clear()
print(backup)
print(num)
# Q9Find the length of num.
length = len(num)
print(length)
# Q10Without using count(), count how many times 30 appears using a loop.
num = [40, 10, 30, 20, 30, 50, 20,30]
count=0
for i in num:
    if i ==  30:
        count +=1
print(count)