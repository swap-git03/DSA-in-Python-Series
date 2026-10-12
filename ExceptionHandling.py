value = "abc"

try:
    amount = int(value)
    print(amount)
except ValueError:
    print("Invalid amount; skip this record")


# 2.
amounts = ["100", "abc", "200"]

for i in amounts:
  try:
    number = int(i)
    print(number)
  except ValueError:
    print('invalid amount')


# 3.
amounts = ["100", "-50", "200"]


for i in amounts:
  try:
    number = int(i)
    if number <= 0:   
      raise ValueError('Invalid Amount')
    print(number)
  except ValueError:
    print('Invalid Amount')
    