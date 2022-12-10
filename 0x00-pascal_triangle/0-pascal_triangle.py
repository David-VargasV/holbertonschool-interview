#!/usr/bin/python3

""" Pascal's Triangle """


def pascal_triangle(n):
    """  List of lists of integers """
    t_pascal = []
    for x in range(1, n+1):
        row = []
        for y in range(x):
            if y == 0 or y == x-1:
                n = 1
                row.append(n)
            else:
                n = t_pascal[x-2][y-1] + t_pascal[x-2][y]
                row.append(n)
        t_pascal.append(row)

    return(t_pascal)
