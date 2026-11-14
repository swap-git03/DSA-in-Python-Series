# len()
s = "hello"
print(len(s))  

# max() / min()
arr = [5, 2, 9, 1]

print(max(arr))  # 9
print(min(arr))  # 1

# sum() (dont work on strings)
arr = [1,2,3,4]
print(sum(arr))  # 10

# sorted()
arr = [3,1,4,2]
print(sorted(arr))  # [1,2,3,4]

# type()
x = 5
print(type(x))  # <class 'int'>

# Type Conversion
int("5")      # 5
float("3.5")  # 3.5
str(10)       # "10"
list("abc")   # ['a','b','c']



# 1.Take a list of numbers from user and print:
# 1. length
# 2. maximum
# 3. minimum
# 4. sum

nums = list(map(int, input("Enter nums : ").split()))
print("Lenght of num is",len(nums));
print("Maximum length of num is", max(nums));
print("Minimum length of num is", min(nums));
print("Sum of numbers is", sum(nums));

# 2.Take a list of numbers and print:
# 1. sorted list
# 2. original list

nums = list(map(int, input("Enter your num : ").split()))
print(f"The original numbers are{nums}")
print(f"The sorted numbers are{sorted(nums)}")

# Q3: Take a list of numbers and print the largest and second largest number. 
nums = list(map(int, input("Enter a number : ").split())) 
maximum = max(nums) 
print(maximum) 
nums.remove(maximum) 
second_maximum = max(nums) 
print(second_maximum)

# Q4: Take a list of numbers and print only the even numbers from the list.
nums = list(map(int, input("Enter your number : ").split()))
for i in nums:
    if i % 2 == 0:
        print(i);


# Q5: Take a list of numbers and count how many even and odd numbers are present.
nums = list(map(int, input("Enter your number : ").split()))
even = 0;
odd = 0;
for i in nums :
    if i % 2 == 0 :
        even = even + 1

    else :
        odd = odd + 1
print(f"The odd numbers in given string are {odd}")
print(f"The even numbers in given string are {even}")

# Q6: Take a list of numbers and print the sum of only even numbers.
nums = list(map(int, input("Enter your number : ").split()))
sum = 0;
for i in nums :
    if i % 2 == 0 :
        sum = i + sum
print(sum)

# Q7: Take a list of numbers and print the reverse of the list (without using built-in reverse()).
nums = list(map(int, input("Enter your number : ").split()))
# rev = 0;

for i in range(len(nums)-1, -1, -1) :
    nums[i]
    print(nums[i], end=" ")

# Q8: Take a list of numbers and print only the unique elements (remove duplicates).
nums = set(map(int, input("Enter your number : ").split()))
print(nums)
# ------------------or--------------------
nums = list(map(int, input("Enter your number : ").split()))
unique = []
for i in nums :
    if i not in unique:
        unique.append(i)
print(unique)