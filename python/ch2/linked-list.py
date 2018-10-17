# simple linked list implementation

class Node(object):
	def __init__(self, data):
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

class DoubleNode(Node):
	def __init__(self, data):
		self.next = None
		self.prev = None
		self.data = data

	def traversebackward(self):
		
		while node != None:
			print(node.data)
			node = node.prev
