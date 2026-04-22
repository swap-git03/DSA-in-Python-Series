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