#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        upperword = str[i]
        if ord(str[i]) > 96 and ord(str[i] < 123):
            upperword = chr(ord(str[i]) - 32)
            print("{}".format(upperword), end='')
    print()
