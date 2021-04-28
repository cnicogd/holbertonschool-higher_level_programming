#!/usr/bin/python3
for number in range(0, 100):

    decimal = number / 10
    unit = number % 10

    if decimal < unit and decimal != unit and number != 89:
        print("{:02d}, ".format(number), end='')

    if number == 89:
        print("{}".format(number))
