'''
Problem: Design algo to remove duplicate characters in string without using any addition buffer.

One or two additional vars is fine, but not an extra copy of the array.

Soln 1: Sort string first with O(nlogn) and then loop through string

Soln 2: Create dictionary/hashmap of each string and then loop through string 
'''

def soln1(string):
	sorted_string = "".join(sorted(string))
	unique_string = []
	for idx, char in enumerate(sorted_string):
		if idx == 0:
			unique_string.append(char)
		else:
			if char != unique_string[-1]:
				unique_string.append(char)
	
	print "string is: ", string
	print "unique is: ", "".join(unique_string)
	return "".join(unique_string)

def soln2(string):
	unique_string = dict()

	for char in string:
		if char not in unique_string:
			unique_string[char] = 1

	print "string is: ", string
	print "unique is: ", "".join(unique_string.keys())
	return "".join(unique_string.keys())

def test():
	soln1('hiiiii')
	soln1('this isatest')
	soln1('zsddfwea')

	soln2('hiiiii')
	soln2('this isatest')
	soln2('zsddfwea')
if __name__ == "__main__":
	test() 