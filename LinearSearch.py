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