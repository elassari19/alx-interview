#!/usr/bin/python3
''' create a pascal triangle method that returns a list of integers'''


def pascal_triangle(n):
	''' returns a list of integers representing the pascal triangle'''
	k = []
	if n <= 0:
		return k
	k = [[1]]
	for i in range(1, n):
		temp = [1]
		for j in range(len(k[i - 1]) - 1):
			curr = k[i - 1]
			temp.append(k[i - 1][j] + k[i - 1][j + 1])
		temp.append(1)
		k.append(temp)
	return k
