#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    Method that calculates the fewest
    number of operations needed to resultin
    exactly n H characters in the file.
    """
    opertation = 0
    div = 2
    while n > 1:
        while n % div == 0:
            opertation += div
            n = int(n / div)
        div += 1
    return (opertation)
