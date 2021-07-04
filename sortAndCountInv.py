'''
Created on Apr 5, 2021

@author: izakaria
'''
def mergeAndCountSpiltInv(A, C,D):
    i=0
    j=0
    spiltInv = 0
    B = []
    for k in range(0,len(A)): 
        if C[i] < D[j]:
            B[k] = C[i]
            i = i+1
        else:
            B[k] = D[j]
            j = j+1
            spiltInv = spiltInv + len(A)//2 - i + 1
    return         
    
def sortAndCountInv(A):
    if len(A) == 0 or len(A) == 1:
        return (A,0);
    else:
        totalN = len(A)
        spiltN = len(A)//2
        C,leftInv = sortAndCountInv(A[0:spiltN])
        D,rightInv = sortAndCountInv(A[spiltN+1:])
        B,spiltInv = mergeAndCountSpiltInv(A[0:totalN], C, D)
        return (B, leftInv + rightInv + spiltInv)


if __name__ == '__main__':
    
    A = [1,3,5,2,4,6]
    (outPut, splitCount) = sortAndCountInv(A)
    print("outPut= ", outPut)
    print("Spiltin Inv=  ", )
    pass
