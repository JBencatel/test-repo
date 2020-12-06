"""
--- Day 1: Report Repair ---

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""

import csv


""" Getting the data in a readable format """
data = []

with open("data.csv", newline = '') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dataItem = int(row[0])
        # print(dataItem)
        data.append(dataItem)


""" Checking which two entries sum to 2020 """

firstValue = 0
secondValue = 0
numberOfOptions = len(data)

for i in range(numberOfOptions):
    a = data[i]
    for j in range(i + 1, numberOfOptions):
        b = data[j]
        result = a + b
        # print( str(a) +  " + " + str(b) + " = " + str(result))
        if result == 2020:
            firstValue = a
            secondValue = b
            break
    if firstValue != 0 & secondValue != 0:
        break

# print(firstValue)
# print(secondValue)


""" Getting the result of multiplying our values """

finalScore = firstValue * secondValue
print(finalScore)

