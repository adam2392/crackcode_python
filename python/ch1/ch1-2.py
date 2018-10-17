'''
Problem: Implement an algorithm to determine reverse a C style-string

- Have to examine each character, no matter how many O(n)
- 

Consider ASCII sets
Solutions:
1. store all existing chars, and keep count of chars. Any count > 1 means there is not all unique characters. Use an array for each index to store count. 
Or use a dictionary/hash where keys are the characters and value are the counts

2. sort through the string and then compare i and i+1 character
'''
import argparse

def reverse(string):
	strlen = len(string)

	# list holder for the reversed string
	reversed_str = []
	for i in range(0,strlen):
		reversed_str.append(string[strlen-i-1])
	print(''.join(reversed_str))
	return ''.join(reversed_str)

def test():
	print "These are tests for reversing strings."

	reverse("aa,'b")
	reverse("hiii")
	reverse("main")

	print "Done testing!"
if __name__ == "__main__":
	test()