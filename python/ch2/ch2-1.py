'''
Problem: Write code to remove duplicates from an unsorted linked list 

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

Notes:

Soln 1: Brute force (loop through entire linked list and keep dictionary of values)

Soln 2: Use two pointers looping through the linked list if necessary.

'''

def isSubstring(s1, s2):
	pass

def removeduplicates(linkedlist):
	valsfound = dict()

	# loop through nodes of linked list
	for node in linkedlist:
		data = node.data

		if data not in valsfound.keys():
			valsfound[data] = 1
			prev = node
		else:
			# remove this node
			node.data = None

			if case == 'double':
				# reset the previous node's next
				node.prev.next = node.next
				# set the next node's prev
				node.next.prev = node.prev
			elif case == 'single':
				prev.next = node.next

	return linkedlist


def test():
	pass
if __name__ == "__main__":
	test() 