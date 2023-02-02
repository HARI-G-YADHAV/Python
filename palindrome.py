def palindrome(s):
	if len(s) == 1 :
		return True
	else:
		if s[0].lower() == s[-1].lower() :
			return palindrome(s[1:-1])
		else:
			return False
s = input("Enter the string: ")
if palindrome(s) == True :
	print("Given string is palindrome")
else :
	print("Given string is not palindrome")

