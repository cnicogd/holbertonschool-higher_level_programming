#!/usr/bin/python3
def print_last_digit(n):
    if n > 0:
        last = n % 10
    else:
        last = (n * -1) % 10
    print("{}".format(last), end='')
    return last
