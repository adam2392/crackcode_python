'''
Problem: Implement an algorithm to find the nth to last element of a singly linked list

Notes:

Soln 1: Set two pointers, push one up to the end

'''


def getnthlastelement(head, n):
	point1 = head
	point2 = head
	for i in range(n):
		point1 = point1.next

	while point1.next != None:
		point1 = point1.next
		point2 = point2.next
	return point2.data

def recursive(node, pos, i=0):
	result = node

	if node ! = None:
		result = recursive(node.next, pos)

		i += 1
		if i == pos:
			result = node

	return result

def test():
	pass
if __name__ == "__main__":
	test() 