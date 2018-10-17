'''
Problem: Design algorithm to replace all spaces in a string with %20

Soln 1: Loop through string and keep track of length to add

Soln 2: 
'''

def soln1(string):
	numinserted = 0

	for idx, char in enumerate(string):
		if char == ' ':
			index = idx + 2*numinserted

			if index < len(string) - 1:
				string = string[:index] + "%20" + string[index+1:]
			elif index == len(string) - 1:
				string = string[:index] + "%20"
			elif index == 0:
				string = "%20" + string[1:]

			numinserted += 1
	print string
	return string

def test():
	soln1('hi this is me')
	soln1('hi')
	soln1('  bla')

if __name__ == "__main__":
	test()