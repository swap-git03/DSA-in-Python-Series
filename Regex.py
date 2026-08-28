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
