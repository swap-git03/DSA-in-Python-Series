
# Take a list of numbers  
# Count frequency of each number

num = list(map(int, input().split()))
d = {}
for i in num:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
print(d)