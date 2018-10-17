'''
Problem: Implement an algorithm to determine if a string has all unique characters. 

- Have to examine each character, no matter how many O(n)
- 

Consider ASCII sets
Solutions:
1. store all existing chars, and keep count of chars. Any count > 1 means there is not all unique characters. Use an array for each index to store count. 
Or use a dictionary/hash where keys are the characters and value are the counts

2. sort through the string and then compare i and i+1 character
'''
import argparse

def isunique_hash(string):
	char_counts = {} # create a dict to hold all counts

	for char in string:
		if char in char_counts:
			return False
		else:
			char_counts[char] = 1

	return True

def isunique_sort(string):
	sorted_string = ''.join(sorted(string))
	print "Sorted word is: ", sorted_string

	for i in range(0, len(sorted_string) - 1):
		char = sorted_string[i]
		next_char = sorted_string[i+1]
		if char == next_char:
			return False
	return True

def test():
	print "These are tests for determining uniqueness of string"

	isunique_hash("aab")
	isunique_hash("hiii")
	isunique_hash("main")

	isunique_sort("aab")
	isunique_sort("hiii")
	isunique_sort("main")

	print "Done testing!"
if __name__ == "__main__":
	test()