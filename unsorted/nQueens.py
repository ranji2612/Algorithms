class Solution(object):
    cur = []
    res = []
    def place(self, queen, row):
        for i in range(queen):
            if row == self.cur[i] or abs(queen-i)==abs(row - self.cur[i]):
                return False
        #print '-----',queen,row
	return True
    
    def addToRes(self,n):
        #make nxn matrix
        x = [ ('.'*n) for j in range(n)]
        for i in range(n):
            x[self.cur[i]] = x[self.cur[i]][:i] + 'Q' + x[self.cur[i]][i+1:]
        self.res.append(x)
        #for i in x:
        #    print i
	
    def NQueens(self, queen, n):
        for row in range(n):
            if(self.place(queen,row)):
                
                self.cur[queen] = row
                if(queen==n-1):
                    #Add to result
                    self.addToRes(n)
                else:
                    self.NQueens(queen+1,n)
    
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.cur = []
        self.cur = [ -1 for i in range(n)]
        self.NQueens(0,n)
        return self.res
        
