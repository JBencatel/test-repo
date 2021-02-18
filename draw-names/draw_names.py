import random

print('Welcome to the Randomizer!!')
print('To start, add the values from which you want to select by writing each one and pressing Enter')

inputValue = ""

options = []

helpInstructions = [
    'To run the Randomizer, write "run" and press Enter',
    'To reset the values, write "reset" and press Enter',
    'To exit the program, write "exit" and press Enter',
]

while True:
    inputValue = input()
    if (inputValue == 'help'):
        for instruction in helpInstructions:
            print(instruction)
    elif (inputValue == 'run'):
        print(random.choice(options))
        break
    elif (inputValue == 'reset'):
        options = []
        print("List reset successfully!")
        print("You can now add a new set of values.")
    elif (inputValue == 'exit'):
        break
    else:
        options.append(inputValue)