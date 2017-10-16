def maxSum(M):
    n = len(M)
    iMax = 0
    jMax = 1
    if M[jMax] < M[iMax]:
        iMax = 1
        jMax = 0
    
    for i in range(2,n):
        if M[i] > M[jMax]:
            if M[i] > M[iMax]:
                iMax = i
            else:
                jMax = i
                
    return(iMax,jMax)



M = [570,111,3,6,3,1200,4,6,7,13,43,23,600]

print(maxSum(M))
        
