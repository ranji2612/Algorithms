
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BST(object):
    def __init__(self):
        self.root = None
    #Internal
    def printNode(self,node):
        print node.val
    def inOrderTraversal(self,node):
        if node==None:
            return
        self.inOrderTraversal(node.left)
        self.printNode(node)
        self.inOrderTraversal(node.right)
    #public
    def inOrder(self):
        self.inOrderTraversal(self.root)
    
    def insert(self,x):
        x = TreeNode(x)
        if self.root==None:
            self.root = x
            return
        i = self.root
        j = None
        while i!=None:
            j = i
            print i.val,x.val
            if i.val > x.val:
                print 'Going left at ',i.val,x.val
                i = i.left
                
            else:
                print 'Going right at ',i.val
                i = i.right
        
        if j.val > x.val:
            j.left = x
        else:
            j.right = x
        return
def inOrder(node):
    if node== None:
        return
    inOrder(node.left)
    print node.val
    inOrder(node.right)
    return
    
def inOrderNew(node,x,y):
    if node== None:
        return
    print 'Function Called',node.val
    
    if node.val-x > 0:
        inOrderNew(node.left,x,y)
    if(node.val >=x and node.val <=y):
        print node.val
    
    if int(node.val) - y < 0:
        inOrderNew(node.right,x,y)
    return

t =  TreeNode(7);
t1 =  TreeNode(3);
t2 =  TreeNode(2);
t3 =  TreeNode(4);

a = BST()
a.insert(7)
a.insert(3)
a.insert(4)
a.insert(2)
a.inOrder()
#inOrder(a.root)
a.insert(10)
a.inOrder()
a.insert(8)
a.inOrder()

"""
import math
#Problem 1
def printSmall(A,x,i):
    print x,i
    if i >= len(A) or A[i]>=x:
        return []
    return [A[i]] + printSmall(A,x,2*i+1) + printSmall(A,x,2*i + 2)
"""


    