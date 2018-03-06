'''
Implement a function to check if a tree is balanced For the purposes of this question, 
a balanced tree is de ned to be a tree such that
 no two leaf nodes di er in distance from the root by more than one

Soln 1: Assume, tree has all properties necessary, traverse tree

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