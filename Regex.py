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