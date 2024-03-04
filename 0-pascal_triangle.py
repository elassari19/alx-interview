#!/usr/bin/python3
''' create a pascal triangle method that returns a list of integers'''


def pascal_triangle(n):
    ''' returns a list of integers representing the pascal triangle'''
    p = []
    if n <= 0:
        return p
    p = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(p[i - 1]) - 1):
            curr = p[i - 1]
            temp.append(p[i - 1][j] + p[i - 1][j + 1])
        temp.append(1)
        p.append(temp)
    return p
