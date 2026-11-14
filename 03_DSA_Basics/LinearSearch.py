# Write a function:
# find_number(numbers, target)  It should return the index if the target exists, otherwise -1.
numbers = [12, 7, 25, 19, 30, 4]

def find_number(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

res = find_number(numbers, 30)
print(res)


# It should return the maximum value.
def find_max(numbers):
    maxi = numbers[0]

    for i in range(len(numbers)):
        if numbers[i]>maxi:
            maxi = numbers[i]
    return maxi

numbers = [17, 4, 29, 11, 35, 8]
result = find_max(numbers)
print(result)


# It should return how many elements are strictly greater than target.

def count_greater(nums, target):
    count = 0
    for i in nums:
        if i> target:
            count +=1
    return count

nums=[10,20,30,40,50]
res = count_greater(nums,20)
print(res)


# It should return how many elements are strictly even and greater than target.
def count_greater(nums, target):
    count = 0
    for i in nums:
        if i%2==0:
            if i> target:
                count +=1
    return count

nums=[10,20,30,41,50]
res = count_greater(nums,20)
print(res)

# Given a list of numbers, find the first even number greater than target and return its index. If no such number exists, return -1.
def find_first_even_greater(nums, target):    
    for i in range(len(nums)):
        if nums[i] % 2==0:
            if nums[i]> target:
                return i
    return -1

nums = [11, 15, 22, 25, 30, 41]
res = find_first_even_greater(nums,20)
print(res)

# return True if any duplicate exists
# return False if all elements are unique
def has_duplicate(nums):
    seen = set()

    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)

    return False

# "Which is the first duplicate we encounter?"
def has_duplicate(nums):
    seen = set()

    for i in nums:
        if i in seen:
            return i
        else:
            seen.add(i)

    return -1
nums = [5, 3, 8, 3, 2, 5]
res=has_duplicate(nums)
print(res)