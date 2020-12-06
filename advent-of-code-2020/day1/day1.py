"""
--- Day 1: Report Repair ---

--- Part One ---

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

#  Getting the data in a readable format
def get_list_of_values():
    dataset = []
    with open("data.csv", newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dataItem = int(row[0])
            # print(dataItem)
            dataset.append(dataItem)
    return dataset

data = get_list_of_values()

# Checking which two entries sum to 2020
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

print(firstValue)
print(secondValue)


# Getting the result of multiplying our values
finalScore = firstValue * secondValue
print(finalScore)




""" 
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""

# Checking which three entries sum to 2020
def get_number_that_sum_to_given_value(numberOfItems, sum):
    items = [0] * numberOfItems
    return start_loop(items, numberOfItems, 0, len(data), sum)
    

# Recursive method to created as many loops as items to discover
def start_loop(items, numberOfItems, start, end, sum):
    for i in range(start, end):
        value = data[i]
        items[start] = value

        if start < numberOfItems-1:
            result = start_loop(items, numberOfItems, start + 1, end, sum)
            if result:
                return result
        
        else:
            result = 0
            for item in items:
                result += item

            if result == sum:
                return items


trioOfValues = get_number_that_sum_to_given_value(3, 2020)
print(trioOfValues)

# Calculates the final value when multiplying a set of numbers
def multiplicate_values(values):
    result = 1
    for value in values:
        result = result * value
    return result

finalResult = multiplicate_values(trioOfValues)
print(finalResult)


# Checking if the new methods work for the first exercise
pairOfValues = get_number_that_sum_to_given_value(2, 2020)
print(pairOfValues)
finalResult = multiplicate_values(pairOfValues)
print(finalResult)



