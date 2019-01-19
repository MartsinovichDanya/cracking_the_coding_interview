'''
Given two strings, write a method to decide if one is a permutation of
the other.
'''

first = input()
second = input()
if len(first) != len(second):
	print(False)
else:
	for ltr in first:
		if first.count(ltr) != second.count(ltr):
			print(False)
			break
	else:
		print(True)

