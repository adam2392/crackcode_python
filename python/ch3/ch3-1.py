'''
Describe how you could use a single array to implement three stacks

Soln 1: 

'''
# simple linked list implementation
class Node(object):
	def __init__(self, data=None):
		self.next = None
		self.data = data

class Stack(object):
	def __init__(self, data=None):
		self.next = None
		self.data = data

	@staticmethod
	def push(stack, val):
		newstack = Stack(val)
		newstack.next = stack

def create3stacks(arr):
	end1 = len(arr)//3
	end2 = 2*len(arr)//3
	end3 = len(arr)



def test():
	pass
if __name__ == "__main__":
	test() 