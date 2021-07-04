'''
Created on July 4, 2021

@author: izakaria
'''

def swap(A, s1 , s2 ):
    tmp = A[s1]
    A[s1] = A[s2]
    A[s2] = tmp
    return A

def pivMedian(A):
    n = len(A)
     
    if n%2 == 0:
        medianPos = (n/2)-1
    else:
        medianPos = (n//2)
    
    if (A[0] > A[n-1] and A[0] < A[medianPos]) or (A[0] > A[medianPos] and A[0] < A[n-1]):
        return 0
    elif (A[n-1] > A[0] and A[n-1] < A[medianPos]) or (A[n-1] > A[medianPos] and A[n-1] < A[0]):
        return n-1
    else:
        return medianPos

def choosePivotPos(A, type):
    n = len(A)
    if type == 1:
        # first pivot
        pivPos = 0
    elif type == 2:
        # last pivot
        pivPos = n-1
    else:
        pivPos = pivMedian(A)    
    return pivPos

def partition(A):
    p = A[0]
    r = len(A)
    i = 1
    
    for j in range(1,r):
        if A[j] < p:
            A = swap(A,i,j)
            i +=1
    A = swap(A,0,i-1)
    return A,i-1
    
def quickSortAlg(A, pivotType):
    n = len(A)
    
    if n>1:
        p = choosePivotPos(A, pivotType)
        A = swap(A,0,p)
        A,pivotPos = partition(A)
        A[:pivotPos], l = quickSortAlg(A[:pivotPos], pivotType)
        A[pivotPos+1:], r = quickSortAlg(A[pivotPos+1:], pivotType)
        return A, l+r+n-1
    else:
        return A,0


if __name__ == '__main__':
    
    with open('QuickSort.txt') as f:
        a = [int(x) for x in f]
        
    (outPut, splitCount) = quickSortAlg(a, 3)
  #  print("outPut= ", outPut)
    print("Spiltin Inv=  ", splitCount)
    pass
