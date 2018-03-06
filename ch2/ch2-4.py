'''
You have two numbers represented by a linked list, 
where each node contains a single digit The digits 
are stored in reverse order, such that the 1’s digit is 
at the head of the list Write a function that adds the two
 numbers and returns the sum as a linked list
EXAMPLE
Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
Notes:

Soln 1: Loop through the longer linked list and add up each node's data

'''
# simple linked list implementation

class Node(object):
	def __init__(self, data=None):
		self.next = None
		self.data = data

	def traverse(self):
		''' 
		O(n) to print out entire list
		'''
		node = self
		while node != None:
			print(node.data)
			node = node.next

def addnumbers(node1, node2):
	if node1 == None and node2 == None:
		return 0

	# initialize resuling linked list
	result = Node()
	buff = result

	# loop through first linked list
	while(node1.next != None):
		result.data = node1.data
		result.next = Node()
		result = result.next

		node1 = node1.next

	result = buff
	while(node2.next != None):
		result.data += node2.data
		result = result.next
		node2 = node2.next
	return result

def addnumbers(node1, node2, carry=0):
	if node1 == None and node2 == None:
		return None
		
	result = Node()
	value = carry

	if node1 != None:
		value += node1.data
	if node2 != None:
		value += node2.data

	result.data = mod(value, 10)
	if value >= 10:
		carryval = 1
	else:
		carryval = 0
	more = addnumbers(node1.next, node2.next, carryval)
	result.next = more
	return result
def test():
	pass
if __name__ == "__main__":
	test() 