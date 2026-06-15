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


# 62. Remove duplicates from a list while preserving order.
nums = [110,20,30,20,50,60,70,10,90,10]
new_nums = list()
for i in nums:
    if i not in new_nums:
        new_nums.append(i)
print(new_nums)


# 64. Merge two lists and remove duplicates.
l1 = [1,2,3,4]
l2= [5,6,7,1]
l3 = l1 + l2
new_list = []
for i in l3:
    if i not in new_list:
        new_list.append(i)
print(new_list)