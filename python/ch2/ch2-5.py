'''
Given a circular linked list, implement an algorithm 
which returns node at the begin- ning of the loop
DEFINITION
Circular linked list: A (corrupt) linked list in which 
a node’s next pointer points to an earlier node, so as 
to make a loop in the linked list

EXAMPLE
input: A -> B -> C -> D -> E -> C [the same C as earlier]
output: C

Soln 1: Use two pointers that iterate through the linkedlist, but
one with speed of 1 and
one with speed of 2 through the next.next

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