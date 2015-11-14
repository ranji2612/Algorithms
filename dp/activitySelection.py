def weightedActivitySelection(act):
    # We have assumed that the activities are already sorted in the order 
    l = len(act)
    
    D =[0 for i in range(l+1)]
    A =[(0,False) for i in range(l+1)]
    
    def bs(e,s,ed,x):
        if s>=ed:
            return s
        m = (s+ed)/2
        if e[m][1]==x:
            return m
        elif e[m][1]>x:
            return bs(e,s,m-1,x)
        else:
            return bs(e,m+1,ed,x)
    for i in range(len(act)):
        j=0
        #Binary Search to find the last ending activity before the start time of the current activity
        j = bs(act,0,l-1,act[i][0])+1
        a = act[i][2] + D[j]
        b = D[i]
        if a >=b:
            D[i+1] = a
            A[i+1] = (j,True)
        else :
            D[i+1] = b
            A[i+1] = (i-1,False)
        #D[i+1] = max(act[i][2] + D[j],D[i])
    
    #Activity Path backtracking
    p =[]
    
    k = l
    while A[k][0] != 0:
        if A[k][1]:
            p.insert(0,k)
        if k==1:
            break
        k = A[k][0]
        
    
    print 'Max Weight for activity ->', D[-1]
    print 'Activities -> ', p
    return D[-1]