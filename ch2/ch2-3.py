'''
Problem: Implement an algorithm to delete a node in the middle of a single linked list, 
given only access to that node
EXAMPLE
Input: the node ‘c’ from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e

Notes:

Soln 1: Get the next node's pointer and data
Set that node's properties to this node

Without having access to the rest of the linkedlist, this would fail if we wanted to delete
the very end, or if the linkedlist was empty.

-> relies on getting the "next node"

'''

def deletenode(node):
	if node == None or node.next == None:
		return 0 # failed if at end

	nextnode = node.next
	node.data = nextnode.data
	node.next = nextnode.next 
	return 1

def test():
	pass
if __name__ == "__main__":
	test() 