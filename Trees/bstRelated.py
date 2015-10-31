def getElements(A,i,x):
	#Reach until the node it becomes bigger 
	#elements of i 
	if i>= len(A) or A[i] >= x:
		return
	else:
		print A[i]
		getElements(A,2*i+1,x)
		getElements(A,2*i+2,x)

import bst
def findNextBiggerNode(T, x, prev):
	if (T == None):
		return prev
	if (T.val == x):
		return T.val
	if (T.val > x):
		#only if its bigger we move to left
		return findNextBiggerNode(T.left, x, T.val)
	else:
		return findNextBiggerNode(T.right,x,prev)

def findNextSmallestNode(T, x, prev):
	if (T== None):
		return prev
	if (T.val == x):
		return T.val
	if (T.val >x):
		return findNextSmallestNode(T.left,x,prev)
	else:
		#Only if its equal or small we move right
		return findNextSmallestNode(T.right,x,T.val)
def printAllElements(T , x, y):
	if (T== None):
		return
	if (T.val > x):
		printAllElements(T.left, x , y)
	if (T.val >=x and T.val <= y):
		print T.val
	if (T.val < y):
		printAllElements(T.right, x, y)
getElements([4,7,5,9,8,5],0,8)
