def rodCutting(prices, n):
    D = [0 for i in range(n+1)]
    prices=[0]+prices
    #D[0] = prices[0]
    for i in range(1,n+1):
        D[i] = prices[i]
        for j in range(1,i+1):
            D[i] = max(D[i],D[i-j]+prices[j])
    return D[n]

def genRodCutting(prices, n):
    #Prices is list of tupes of length & value
    D = [0 for i in range(n+1)]
    p = {}
    for (length,value) in prices:
        p[length] = value
    
    for i in range(1,n+1):
        D[i] = prices[i]
        for j in range(1,i+1):
            D[i] = max(D[i],D[i-j]+prices[j])
    return D[n]