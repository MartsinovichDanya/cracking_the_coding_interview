''' 
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use editional data structures?
'''
s = input().lower() # if uppercase and lowercase letters are the same
# if not - s = input()
for ltr in s:
	if s.count(ltr) > 1:
		print(False)
		break
else:
	print(True)

