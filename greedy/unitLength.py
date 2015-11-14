def smallestSetUnitLength(p):
    p.sort()
    s = p[0]
    noOfSet = 1
    clasSet = [[p[0]]]
    #Greedily assigning intervals
    for i in range(1,len(p)):
        if p[i]-s > 1:
            #Next set
            s = p[i]
            noOfSet+=1
            #To maintain the boundaries and elements
            clasSet.append([p[i]])
        else:
            clasSet[-1].append(p[i])
    print clasSet
    return noOfSet
            