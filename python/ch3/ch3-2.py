'''
How would you design a stack which, 
in addition to push and pop, also has a function min
which returns the minimum element? Push, pop and min 
should all operate in O(1) time

Soln 1: Store the min element pointer at the top of the stack

'''
# simple linked list implementation
import math

class StackWithMin(object):
	def __init__(self):
		self.stack = []
		self.min = []

	def push(self, val):
		self.stack.append(val)
		if not self.min or val <= self.min:
			self.min.append(val)

	def pop(self):
		val = self.stack.pop()
		if val == self.min:
			self.min.pop()
		return val

def test():
	pass
if __name__ == "__main__":
	test() 