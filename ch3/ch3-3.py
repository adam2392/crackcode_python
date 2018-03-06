'''
Imagine a (literal) stack of plates If the stack gets too high, 
it might topple There- fore, in real life, we would likely start
 a new stack when the previous stack exceeds some threshold
  Implement a data structure SetOfStacks that mimics this 
  SetOf- Stacks should be composed of several stacks, and 
  should create a new stack once the previous one exceeds 
  capacity SetOfStacks push() and SetOfStacks pop() should 
  behave identically to a single stack (that is, pop() should
   return the same values as it would if there were just a single stack)

FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a speci c sub-stack
Soln 1: 

'''
# simple linked list implementation

THRESH = 300

class Stack(object):
	def __init__(self, data=None):
		self.next = None
		self.data = data

class SetOfStacks(object):
	def __init__(self):
		self.listofstacks = []

	def pop(self):
		val = self.listofstacks[-1].pop()
		if len(self.listofstacks[-1]) == 0:
			self.listofstacks.pop()
		return val
	def push(self, val):
		if len(self.listofstacks[-1]) > THRESH:
			self.listofstacks.append(Stack(val))
		else:
			self.listofstacks[-1].append(val)



def test():
	pass
if __name__ == "__main__":
	test() 