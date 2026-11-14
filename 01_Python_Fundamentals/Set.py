# Q1 Create:
# nums = {10, 20, 30, 20, 40, 10, 50}
# Print it and observe what happens to duplicates.
nums = {10, 20, 30, 20, 40, 10, 50}
print(nums)


# Q2 Add 60.
nums.add(60)
print(nums)


# Q3 Add 70, 80, 90 using one operation.
nums.update([70,80,90])
print(nums)


# Q4 Remove 30 using remove().
nums.remove(30)
print(nums)

# Q5 Given:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a|b)
print(a&b)
# Find: Union,Intersection
# Symmetric difference
print(a^b)

# Q6 Check whether 3 exists in A.
print(3 in a)

# Q8 — Given:
nums = [10, 20, 10, 30, 20, 40, 30]
# Remove duplicates using a set.
newset = set(nums)
print(newset)