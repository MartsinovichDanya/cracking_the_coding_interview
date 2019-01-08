s = input().lower() # if uppercase and lowercase letters are the same
# if not - s = input()
for ltr in s:
	if s.count(ltr) > 1:
		print(False)
		break
else:
	print(True)

