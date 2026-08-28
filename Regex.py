# \d → digit
# \D → NOT a digit

# \w → word character
# \W → NOT a word character

# \s → whitespace
# \S → NOT whitespace

# search() : Finds the first match.
# findall(): Finds all matches.

import re
text = """
Customer Rahul
Phone: 9876543210

Customer Amit
Phone: 8765432109
"""
phones = re.findall(r"\d{10}", text)
print(phones)

# Find all digits using findall().
text = "I have 3 apples and 5 oranges"
digits = re.findall(r"\d{1}", text)
print(digits)

# Extract all complete numbers.
text = "Order 123 costs 450 and order 456 costs 700"
res = re.findall(r"\d+", text)
print(res)

# Extract only numbers containing exactly 5 digits.
text = "IDs: 12345, 987654, 45678"
res = re.findall(r"\d{5}", text)
print(res)

# Find all words beginning with either c, b, or r.
text = "cat bat rat mat dog"
res = re.findall(r"[cbr]at", text)
print(res)

# Find all uppercase letters individually.
text = "Rahul BDA SQL Python"
res = re.findall(r"[A-Z]", text)
print(res)

# Find all characters that are NOT letters or digits.
text = "abc123@#$xyz"
res = re.findall(r"[^a-zA-Z0-9]",text)
print(res)


# Q7 — Check whether strings start with "Python"
texts = ["Python is easy", "I love Python", "Python123"]

for text in texts:
    result = re.match(r"Python", text)

    if result:
        print(text, "→ Yes")
    else:
        print(text, "→ No")

# Q8 — Check whether strings end with ".com"

texts = [
    "google.com",
    "gmail.com",
    "google.in",
    "example.com.in"
]

for text in texts:
    result = re.search(r"\.com$", text)

    if result:
        print(text, "→ Yes")
    else:
        print(text, "→ No")

# Q9 — Find cat or dog
text = "I have a cat, dog, cow and another cat"
result = re.findall(r"cat|dog", text)
print(result)


# Q10 — Find first sequence of digits
text = "My employee ID is BDA12345"
result = re.search(r"\d+", text)
print(result.group())

# Q11 — Extract all marks
text = "Marks: 85, 92, 76, 90"
result = re.findall(r"\d+", text)
print(result)

# Q12 — finditer()
text = "I have 123 apples and 456 oranges"
results = re.finditer(r"\d+", text)
for match in results:
    print("Value:", match.group())
    print("Starting position:", match.start())


# Q13 — Replace numbers
text = "My PIN is 1234"
result = re.sub(r"\d+", "XXXX", text)
print(result)


# Q14 — Split using multiple separators
text = "apple,banana;orange|mango"
result = re.split(r"[,;|]", text)
print(result)


text = "Rahul has 25 apples, Amit has 30 oranges and Priya has 15 bananas."
# A. Extract numbers
numbers = re.findall(r"\d+", text)
print(numbers)

# B. Extract names
names = re.findall(r"[A-Z][a-z]+", text)
print(names)

# C. Replace numbers
new_text = re.sub(r"\d+", "XX", text)
print(new_text)