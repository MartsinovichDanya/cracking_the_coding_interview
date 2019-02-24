'''
Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.
'''

def compress(s):
	result = ''
	cur_ltr = s[0]
	counter = 0
	for ltr in s:
		if ltr == cur_ltr:
			counter += 1
		else:
			result += cur_ltr + str(counter)
			cur_ltr = ltr
			counter = 1
	result += cur_ltr + str(counter)
	if len(result) >= len(s):
		return s
	return result


print(compress(input()))

