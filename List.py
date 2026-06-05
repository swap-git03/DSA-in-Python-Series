◆ Beginner

# 61. Create a list of 10 numbers and print max, min, and sum without built-in functions.
nums = [110,20,30,40,50,60,70,80,90,10]
maxi = nums[0]
mini = nums[0]
total = 0
for i in nums:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
    total = total + i
print(maxi, mini, total)
