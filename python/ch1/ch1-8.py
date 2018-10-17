'''
Problem:  Assume you have a method isSubstring which checks 
if one word is a substring of another Given two strings, 
s1 and s2, write code to check if s2 is a rotation of s1 
using only one call to isSubstring 
(i e , “waterbottle” is a rotation of “erbottlewat”)

Notes:
- can't sort strings, since you need the positioning to determine rotation
-

Soln 1: For checking is substring, assume built.
- Concatenate the first string and the second should be part of that string

'''

def isSubstring(s1, s2):
	pass

def isrotation(s1, s2):
	if len(s1) != len(s2):
		return 0

	# concatenate string1 with itself and see if string 2 is a subset
	s1_cat = s1 + s1
	return isSubstring(s1_cat, s2)

def test():
	pass
if __name__ == "__main__":
	test() 