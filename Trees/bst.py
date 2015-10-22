
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
    def _inOrder(self,node):
        if node==None:
            return
        self._inOrder(node.left)
        self.printNode(node)
        self._inOrder(node.right)
    #public
    def traverse(self,method = "inOrder"):
	if (method=="postOrder"):
            self._postOrder(self.root)
	elif (method=="preOrder"):
	    self._preOrder(self.root)
	else:
	    self._inOrder(self.root)
	
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
