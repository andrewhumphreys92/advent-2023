import sys

if len(sys.argv) != 2:
    sys.exit("You forgot your input!")

numbers = []
pairs = []
additions = 0

with open(sys.argv[1], "r") as f:
    reader = f.readlines()
    for line in reader:
        for n in range(len(line)):
            if line[n].isnumeric():
                numbers.append(line[n])

            if line[n:n+4] == "zero":
                numbers.append('0')

            if line[n:n+3] == "one":
                numbers.append('1')

            if line[n:n+3] == "two":
                numbers.append('2')

            if line[n:n+5] == "three":
                numbers.append('3')

            if line[n:n+4] == "four":
                numbers.append('4')

            if line[n:n+4] == "five":
                numbers.append('5')

            if line[n:n+3] == "six":
                numbers.append('6')

            if line[n:n+5] == "seven":
                numbers.append('7')

            if line[n:n+5] == "eight":
                numbers.append('8')

            if line[n:n+4] == "nine":
                numbers.append('9')

        placeholder = int(str(numbers[0]) + str(numbers[-1]))
        additions = additions + placeholder

        numbers = []

    print(additions)
