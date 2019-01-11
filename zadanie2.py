'''
Implement a function void reversefchar* str) in Cor C++ which reverses a null-termi-
nated string.
'''

def reverse(s):
	result_s = ''
	for i in range(len(s) - 1, -1, -1):
		result_s += s[i]
	return result_s

print(reverse(input()))
