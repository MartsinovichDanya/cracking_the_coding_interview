'''
Write a method to replace all spaces in a string with '%20'. You may assume that the
string has sufficient space at the end of the string to hold the additional characters,
and that you are given the "true" length of the string.
'''

def replace_spaces(s):
	s = list(s)
	for i in range(len(s)):
		if s[i].isspace():
			s[i] = '%20'
	return ''.join(s)

print(replace_spaces(input()))
