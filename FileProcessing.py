import csv

with open("orders_input.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

import csv
with open("orders_input.csv", "r", newline="", encoding="utf-8") as file:
    