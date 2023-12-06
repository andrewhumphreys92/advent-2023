import sys

if len(sys.argv) != 2:
    sys.exit("You forgot your input!")

numbers = []
pairs = []
additions = 0

with open(sys.argv[1], "r") as f:
    reader = f.readlines()
    for line in reader:
        for character in line:
            if character.isnumeric():
                numbers.append(character)

        placeholder = int(str(numbers[0]) + str(numbers[-1]))
        additions = additions + placeholder

        numbers = []

    print(additions)
