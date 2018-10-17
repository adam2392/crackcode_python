'''
Given a directed graph, design an algorithm to  nd out whether 
there is a route be- tween two nodes

Soln 1: 

'''

def maxdepth(tree):
	if tree.val == None:
		return 0
	return 1 + max(maxdepth(tree.right), maxdepth(tree.left))

def mindepth(tree):
	if tree.val == None:
		return 0
	return 1 + min(mindepth(tree.right), mindepth(tree.left))

def checkbalance(tree):
	return maxdepth(tree) - mindepth(tree) <= 1

if __name__ == "__main__":
	test() 