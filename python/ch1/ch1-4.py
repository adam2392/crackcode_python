'''
Problem: Implement an algorithm to determine if two strings are anagrams
or not

Option 0:
- Create a dictionary with all the letters of the word that have a count
- Create a dictionary of the second string with all letters of the word
with a count
- loops through each string once. -> O(n)

Option 1:
-> essentially checking if each character in the string occurs in the second
-> can be O(n2) since there are 2 loops, that can loop through the entire two strings
in a nested loop...

Option 2:
- Sort the elements first and compare string O(nlogn) + O(n) = O(nlogn)

'''
import argparse

def soln1(string1, string2):
	# determine if string is an anagram by check off
	alist = list(string1)
	blist = list(string2)

	ind = 0
	isokay = True

	while ind < len(alist) and isokay:
		ind2 = 0
		found = False
		while ind2 < len(alist) and not found:
			if alist[ind] == blist[ind2]:
				found = True
			else:
				ind2 += 1
		if found:
			alist[ind2] = None
			ind += 1
		else:
			isokay = False
	return isokay

def soln0(string1, string2):
	acount = [0]*26
	bcount = [0]*26

	for i in range(len(string1)):
		pos = ord(string1[i]) - ord('a')
		acount[pos] += 1

	for i in range(len(string2)):
		pos = ord(string2[i]) - ord('a')
		bcount[pos] += 1

	j=0
	isokay = True
	while j<26 and isokay:
		if acount[j] != bcount[j]:
			isokay = False
		j += 1
	return isokay

def check_anagram(string1, string2):
	# first check if they are the same len
	if len(string1) != len(string2):
		print(False)
		return 0

	# now check if they are anagrams
	# isanagram = soln1(string1, string2)
	# print(isanagram)
	isanagram = soln0(string1, string2)
	print(isanagram)

def test():
	print "These are tests for reversing strings."

	check_anagram("aab", 'baa')
	check_anagram("hiii", 'ih')
	check_anagram("main", 'maim')

	print "Done testing!"
if __name__ == "__main__":
	test()