# Q1: Convert a value to an integer. If the value is not numeric, catch the
# ValueError and print a message that the record should be skipped.
value = "abc"

try:
    amount = int(value)
    print(amount)
except ValueError:
    print("Invalid amount; skip this record")


# Q2: Given a list of amount strings, convert and print each valid amount.
# If an item cannot be converted to an integer, print "invalid amount" and continue.
amounts = ["100", "abc", "200"]

for i in amounts:
  try:
    number = int(i)
    print(number)
  except ValueError:
    print('invalid amount')


# Q3: Given a list of amount strings, print only positive integer amounts.
# Treat non-numeric values and zero or negative amounts as invalid.
amounts = ["100", "-50", "200"]


for i in amounts:
  try:
    number = int(i)
    if number <= 0:   
      raise ValueError('Invalid Amount')
    print(number)
  except ValueError:
    print('Invalid Amount')

# Q4: Validate each amount string using try, except, else, and finally.
# Print valid positive amounts, report invalid entries, and confirm that every
# record has been checked.
amounts = ["100", "abc", "-50", "200"]

for i in amounts:
  try:
    number = int(i)
    if number <= 0:   
      raise ValueError('Invalid Amount')
  except ValueError:
    print('Invalid Amount')
  else:
    print('Valid Records', number)
  finally:
    print('All records checked')

