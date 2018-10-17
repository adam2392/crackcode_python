'''
Problem:  Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column is set to 0

Soln 1: Brute force entire matrix

Soln 2: Loop through the smaller element
Break when you find a zero and move to the next index


'''

def mungemat_1(mat, m, n):
	rows_tozero = []
	cols_tozero = []

	for i in range(m):
		for j in range(n):
			if mat[i,j] == 0:
				rows_tozero.append(i)
				cols_tozero.append(j)
	for row in rows_tozero:
		mat[row,:] = 0
	for col in cols_tozero:
		mat[:,col] = 0
	return mat

def test():
	pass
if __name__ == "__main__":
	test() 